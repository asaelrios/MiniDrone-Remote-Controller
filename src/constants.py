# Drone Connection
DRONE_IP = "192.168.1.1"
DRONE_PORT = 7099
VIDEO_STREAM_URL = 'rtsp://192.168.1.1:7070/webcam/track0'

# Datagram Structure (indices for the bytearray)
DATAGRAM_START_BYTE = 0x03
DATAGRAM_END_BYTE = 0x99
DATAGRAM_FIXED_BYTE = 0x66 # This byte seems to be fixed in the neutral position
DATAGRAM_THROTTLE_INDEX = 2 # Up/Down
DATAGRAM_ROLL_INDEX = 3     # Left/Right
DATAGRAM_PITCH_INDEX = 4    # Forward/Backward
DATAGRAM_YAW_INDEX = 5      # Turn Left/Right
DATAGRAM_CHECKSUM_INDEX = 7

# PWM Values
PWM_NEUTRAL = 0x80 # 128 in decimal
PWM_MAX = 0xFF      # 255 in decimal
PWM_MIN = 0x00      # 0 in decimal
PWM_STEP = 0x04     # 4 in decimal (for flight commands)
PWM_LANDING_STEP = 5 # For gradual landing

# Key Mappings (for better readability)
KEY_W = 'up'
KEY_S = 'down'
KEY_A = 'turn-left'
KEY_D = 'turn-right'
KEY_I = 'forward'
KEY_K = 'backward'
KEY_J = 'left'
KEY_L = 'right'
KEY_ESC = 'landing'
KEY_BACKSPACE = 'takeoff'