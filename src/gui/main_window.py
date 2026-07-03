from PySide6.QtCore import Qt, QCoreApplication
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QWidget, QMessageBox, QLabel, QLineEdit, QPushButton, QGroupBox
from PySide6.QtUiTools import QUiLoader # Import QUiLoader

import os

from src.core.drone_controller import DroneController
from src.core.video_stream import VideoThread
from src.constants import (
    DATAGRAM_THROTTLE_INDEX, DATAGRAM_ROLL_INDEX, DATAGRAM_PITCH_INDEX, DATAGRAM_YAW_INDEX,
    PWM_NEUTRAL, PWM_STEP,
    KEY_W, KEY_S, KEY_A, KEY_D, KEY_I, KEY_K, KEY_J, KEY_L,
    DRONE_IP, DRONE_PORT, VIDEO_STREAM_URL
)

class DroneMainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Load the user interface directly from the .ui file
        loader = QUiLoader()
        # Ensure the path to the .ui file is correct
        ui_file_path = os.path.join(os.path.dirname(__file__), "drone_interface.ui")
        self.ui = loader.load(ui_file_path, self)

        # Assign loaded widgets to attributes for easy access
        # This is necessary because loader.load() returns the main widget (self),
        # and sub-widgets are not automatically assigned to self.ui as in the case of uic.loadUiType
        self.video_label = self.findChild(QLabel, "video_label")
        self.le_drone_ip = self.findChild(QLineEdit, "le_drone_ip")
        self.le_drone_port = self.findChild(QLineEdit, "le_drone_port")
        self.le_video_url = self.findChild(QLineEdit, "le_video_url")
        self.btn_apply_settings = self.findChild(QPushButton, "btn_apply_settings")

        self.btn_up = self.findChild(QPushButton, "btn_up")
        self.btn_down = self.findChild(QPushButton, "btn_down")
        self.btn_turn_left = self.findChild(QPushButton, "btn_turn_left")
        self.btn_turn_right = self.findChild(QPushButton, "btn_turn_right")
        self.btn_forward = self.findChild(QPushButton, "btn_forward")
        self.btn_backward = self.findChild(QPushButton, "btn_backward")
        self.btn_strafe_left = self.findChild(QPushButton, "btn_strafe_left")
        self.btn_strafe_right = self.findChild(QPushButton, "btn_strafe_right")
        self.btn_land = self.findChild(QPushButton, "btn_land")
        self.btn_takeoff = self.findChild(QPushButton, "btn_takeoff")


        # Set the window title
        self.setWindowTitle(QCoreApplication.translate("DroneInterface", u"MiniDrone Remote Controller", None))


        # Initialize controllers with default values
        self.drone_controller = DroneController(ip=DRONE_IP, port=DRONE_PORT)
        # The video_thread will be initialized with the generated or entered URL
        self.video_thread = VideoThread(video_url=VIDEO_STREAM_URL)

        # Dictionary to keep track of key states
        self.keys_pressed = {
            KEY_W: False, KEY_S: False, KEY_A: False, KEY_D: False,
            KEY_I: False, KEY_K: False, KEY_J: False, KEY_L: False
        }

        self._init_ui_values()
        self._connect_signals()

        # Start the video thread after connecting signals
        self.video_thread.start()

    def _init_ui_values(self):
        """Initializes text fields with constant values."""
        self.le_drone_ip.setText(DRONE_IP)
        self.le_drone_port.setText(str(DRONE_PORT))
        # Call the update function to set the initial video URL
        self._on_drone_ip_changed(DRONE_IP)

    def _connect_signals(self):
        # Connect control button signals to drone controller slots
        self.btn_up.pressed.connect(lambda: self.drone_controller.set_throttle(PWM_NEUTRAL + PWM_STEP * 4))
        self.btn_up.released.connect(lambda: self.drone_controller.reset_datagram_axis(DATAGRAM_THROTTLE_INDEX))
        self.btn_down.pressed.connect(lambda: self.drone_controller.set_throttle(PWM_NEUTRAL - PWM_STEP * 4))
        self.btn_down.released.connect(lambda: self.drone_controller.reset_datagram_axis(DATAGRAM_THROTTLE_INDEX))

        self.btn_turn_left.pressed.connect(lambda: self.drone_controller.set_yaw(PWM_NEUTRAL - PWM_STEP * 4))
        self.btn_turn_left.released.connect(lambda: self.drone_controller.reset_datagram_axis(DATAGRAM_YAW_INDEX))
        self.btn_turn_right.pressed.connect(lambda: self.drone_controller.set_yaw(PWM_NEUTRAL + PWM_STEP * 4))
        self.btn_turn_right.released.connect(lambda: self.drone_controller.reset_datagram_axis(DATAGRAM_YAW_INDEX))

        self.btn_forward.pressed.connect(lambda: self.drone_controller.set_pitch(PWM_NEUTRAL + PWM_STEP * 4))
        self.btn_forward.released.connect(lambda: self.drone_controller.reset_datagram_axis(DATAGRAM_PITCH_INDEX))
        self.btn_backward.pressed.connect(lambda: self.drone_controller.set_pitch(PWM_NEUTRAL - PWM_STEP * 4))
        self.btn_backward.released.connect(lambda: self.drone_controller.reset_datagram_axis(DATAGRAM_PITCH_INDEX))

        self.btn_strafe_left.pressed.connect(lambda: self.drone_controller.set_roll(PWM_NEUTRAL - PWM_STEP * 4))
        self.btn_strafe_left.released.connect(lambda: self.drone_controller.reset_datagram_axis(DATAGRAM_ROLL_INDEX))
        self.btn_strafe_right.pressed.connect(lambda: self.drone_controller.set_roll(PWM_NEUTRAL + PWM_STEP * 4))
        self.btn_strafe_right.released.connect(lambda: self.drone_controller.reset_datagram_axis(DATAGRAM_ROLL_INDEX))

        # Connect action buttons
        self.btn_land.clicked.connect(self.drone_controller.landing)
        self.btn_takeoff.clicked.connect(self.drone_controller.takeoff)

        # Connect video thread signals
        self.video_thread.change_pixmap_signal.connect(self.update_image)
        self.video_thread.stream_error_signal.connect(self._handle_video_stream_error)

        # Connect apply settings button
        self.btn_apply_settings.clicked.connect(self._apply_connection_settings)

        # Connect the textChanged signal of the IP field to autocomplete the video URL
        self.le_drone_ip.textChanged.connect(self._on_drone_ip_changed)

    def _on_drone_ip_changed(self, ip_text):
        """Updates the suggested video URL based on the drone's IP."""
        # Assuming the video stream port is fixed (7070) and the path as well
        suggested_video_url = f"rtsp://{ip_text}:7070/webcam/track0"
        self.le_video_url.setText(suggested_video_url)

    def _apply_connection_settings(self):
        """Applies the new connection settings for the drone and video stream."""
        new_drone_ip = self.le_drone_ip.text()
        new_video_url = self.le_video_url.text()

        try:
            new_drone_port = int(self.le_drone_port.text())
            if not (1 <= new_drone_port <= 65535):
                raise ValueError("Port must be between 1 and 65535.")
        except ValueError as e:
            QMessageBox.critical(self, "Configuration Error", f"Invalid port: {e}")
            return

        # Update DroneController
        self.drone_controller.update_connection(new_drone_ip, new_drone_port)

        # Update VideoThread
        self.video_thread.update_stream_url(new_video_url)

        QMessageBox.information(self, "Settings Applied", "Connection settings have been applied.")

    def _handle_video_stream_error(self, error_msg):
        """Handles errors reported by the video thread."""
        QMessageBox.warning(self, "Video Stream Error", error_msg)
        self.video_label.setText("Error: No Video Feed")

    def update_image(self, qt_image):
        """Updates the image in the GUI."""
        # Scale the image to fit the QLabel
        pixmap = QPixmap.fromImage(qt_image)
        scaled_pixmap = pixmap.scaled(self.video_label.size(),
                                      Qt.AspectRatioMode.KeepAspectRatio,
                                      Qt.TransformationMode.SmoothTransformation)
        self.video_label.setPixmap(scaled_pixmap)

    def keyPressEvent(self, event):
        if event.isAutoRepeat():
            return

        if event.key() == Qt.Key_W and not self.keys_pressed[KEY_W]:
            self.keys_pressed[KEY_W] = True
            self.drone_controller.set_throttle(PWM_NEUTRAL + PWM_STEP * 4)
        elif event.key() == Qt.Key_S and not self.keys_pressed[KEY_S]:
            self.keys_pressed[KEY_S] = True
            self.drone_controller.set_throttle(PWM_NEUTRAL - PWM_STEP * 4)
        elif event.key() == Qt.Key_A and not self.keys_pressed[KEY_A]:
            self.keys_pressed[KEY_A] = True
            self.drone_controller.set_yaw(PWM_NEUTRAL - PWM_STEP * 4)
        elif event.key() == Qt.Key_D and not self.keys_pressed[KEY_D]:
            self.keys_pressed[KEY_D] = True
            self.drone_controller.set_yaw(PWM_NEUTRAL + PWM_STEP * 4)
        elif event.key() == Qt.Key_I and not self.keys_pressed[KEY_I]:
            self.keys_pressed[KEY_I] = True
            self.drone_controller.set_pitch(PWM_NEUTRAL + PWM_STEP * 4)
        elif event.key() == Qt.Key_K and not self.keys_pressed[KEY_K]:
            self.keys_pressed[KEY_K] = True
            self.drone_controller.set_pitch(PWM_NEUTRAL - PWM_STEP * 4)
        elif event.key() == Qt.Key_J and not self.keys_pressed[KEY_J]:
            self.keys_pressed[KEY_J] = True
            self.drone_controller.set_roll(PWM_NEUTRAL - PWM_STEP * 4)
        elif event.key() == Qt.Key_L and not self.keys_pressed[KEY_L]:
            self.keys_pressed[KEY_L] = True
            self.drone_controller.set_roll(PWM_NEUTRAL + PWM_STEP * 4)
        elif event.key() == Qt.Key_Escape:
            self.drone_controller.landing()
        elif event.key() == Qt.Key_Backspace:
            self.drone_controller.takeoff()

    def keyReleaseEvent(self, event):
        if event.isAutoRepeat():
            return

        if event.key() == Qt.Key_W and self.keys_pressed[KEY_W]:
            self.keys_pressed[KEY_W] = False
            self.drone_controller.reset_datagram_axis(DATAGRAM_THROTTLE_INDEX)
        elif event.key() == Qt.Key_S and self.keys_pressed[KEY_S]:
            self.keys_pressed[KEY_S] = False
            self.drone_controller.reset_datagram_axis(DATAGRAM_THROTTLE_INDEX)
        elif event.key() == Qt.Key_A and self.keys_pressed[KEY_A]:
            self.keys_pressed[KEY_A] = False
            self.drone_controller.reset_datagram_axis(DATAGRAM_YAW_INDEX)
        elif event.key() == Qt.Key_D and self.keys_pressed[KEY_D]:
            self.keys_pressed[KEY_D] = False
            self.drone_controller.reset_datagram_axis(DATAGRAM_YAW_INDEX)
        elif event.key() == Qt.Key_I and self.keys_pressed[KEY_I]:
            self.keys_pressed[KEY_I] = False
            self.drone_controller.reset_datagram_axis(DATAGRAM_PITCH_INDEX)
        elif event.key() == Qt.Key_K and self.keys_pressed[KEY_K]:
            self.keys_pressed[KEY_K] = False
            self.drone_controller.reset_datagram_axis(DATAGRAM_PITCH_INDEX)
        elif event.key() == Qt.Key_J and self.keys_pressed[KEY_J]:
            self.keys_pressed[KEY_J] = False
            self.drone_controller.reset_datagram_axis(DATAGRAM_ROLL_INDEX)
        elif event.key() == Qt.Key_L and self.keys_pressed[KEY_L]:
            self.keys_pressed[KEY_L] = False
            self.drone_controller.reset_datagram_axis(DATAGRAM_ROLL_INDEX)

    def closeEvent(self, event):
        """Ensures threads are properly stopped when the application closes."""
        print("Closing application...")
        self.video_thread.stop()
        self.drone_controller.close()
        super().closeEvent(event)