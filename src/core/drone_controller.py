import socket
import time
from src.constants import (
    DRONE_IP, DRONE_PORT, PWM_NEUTRAL, DATAGRAM_START_BYTE, DATAGRAM_FIXED_BYTE,
    DATAGRAM_END_BYTE, DATAGRAM_THROTTLE_INDEX, DATAGRAM_ROLL_INDEX,
    DATAGRAM_PITCH_INDEX, DATAGRAM_YAW_INDEX, DATAGRAM_CHECKSUM_INDEX,
    PWM_STEP, PWM_LANDING_STEP
)

class DroneController:
    def __init__(self, ip=DRONE_IP, port=DRONE_PORT):
        self.udp_ip = ip
        self.udp_port = port
        self.sock = self._create_socket()

        self.neutral_position_datagram = bytearray([
            DATAGRAM_START_BYTE,
            DATAGRAM_FIXED_BYTE,
            PWM_NEUTRAL, # Throttle
            PWM_NEUTRAL, # Roll
            PWM_NEUTRAL, # Pitch
            PWM_NEUTRAL, # Yaw
            0x00, # Placeholder for checksum
            0x00, # Checksum
            DATAGRAM_END_BYTE
        ])
        self.current_datagram = self.neutral_position_datagram[:]

    def _create_socket(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(1) # Set a timeout for sendto operations if needed
        return sock

    def update_connection(self, ip, port):
        if self.udp_ip != ip or self.udp_port != port:
            print(f"Updating drone connection from {self.udp_ip}:{self.udp_port} to {ip}:{port}")
            self.close()
            self.udp_ip = ip
            self.udp_port = port
            self.sock = self._create_socket()
            self.current_datagram = self.neutral_position_datagram[:] # Reset datagram on new connection

    def _calculate_checksum(self, datagram):
        return datagram[DATAGRAM_THROTTLE_INDEX] ^ \
               datagram[DATAGRAM_ROLL_INDEX] ^ \
               datagram[DATAGRAM_PITCH_INDEX] ^ \
               datagram[DATAGRAM_YAW_INDEX]

    def send_command(self, pwm_value, position_index):
        self.current_datagram[position_index] = pwm_value
        self.current_datagram[DATAGRAM_CHECKSUM_INDEX] = self._calculate_checksum(self.current_datagram)
        try:
            self.sock.sendto(self.current_datagram, (self.udp_ip, self.udp_port))
        except socket.timeout:
            print("Socket send timeout. Drone might not be reachable.")
        except Exception as e:
            print(f"Error sending command: {e}")

    def reset_datagram_axis(self, position_index):
        self.current_datagram[position_index] = PWM_NEUTRAL
        self.current_datagram[DATAGRAM_CHECKSUM_INDEX] = self._calculate_checksum(self.current_datagram)
        try:
            self.sock.sendto(self.current_datagram, (self.udp_ip, self.udp_port))
        except socket.timeout:
            print("Socket send timeout. Drone might not be reachable.")
        except Exception as e:
            print(f"Error sending command: {e}")

    def takeoff(self):
        self.send_command(0xFF, DATAGRAM_THROTTLE_INDEX) # Use 0xFF for max throttle
        time.sleep(0.1)

    def landing(self):
        pwm_value = PWM_NEUTRAL
        while pwm_value > PWM_LANDING_STEP:
            pwm_value -= PWM_LANDING_STEP
            self.send_command(pwm_value, DATAGRAM_THROTTLE_INDEX)
            time.sleep(0.1)
        self.send_command(0, DATAGRAM_THROTTLE_INDEX)
        self.current_datagram = self.neutral_position_datagram[:]

    def set_throttle(self, value):
        self.send_command(value, DATAGRAM_THROTTLE_INDEX)

    def set_roll(self, value):
        self.send_command(value, DATAGRAM_ROLL_INDEX)

    def set_pitch(self, value):
        self.send_command(value, DATAGRAM_PITCH_INDEX)

    def set_yaw(self, value):
        self.send_command(value, DATAGRAM_YAW_INDEX)

    def close(self):
        if self.sock:
            self.sock.close()
            self.sock = None
