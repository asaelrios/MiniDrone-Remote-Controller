import cv2
from PySide6.QtCore import QThread, Signal
from PySide6.QtGui import QImage
from src.constants import VIDEO_STREAM_URL

class VideoThread(QThread):
    change_pixmap_signal = Signal(QImage)
    stream_error_signal = Signal(str) # Signal for stream errors

    def __init__(self, video_url=VIDEO_STREAM_URL, parent=None):
        super().__init__(parent)
        self._video_url = video_url
        self._cap = None
        self._running = True

    def run(self):
        self._running = True
        try:
            self._cap = cv2.VideoCapture(self._video_url)
            if not self._cap.isOpened():
                error_msg = f"Error: Could not open camera at {self._video_url}"
                print(error_msg)
                self.stream_error_signal.emit(error_msg)
                self._running = False # Stop running if stream can't be opened
                return

            while self._running and not self.isInterruptionRequested():
                ret, frame = self._cap.read()
                if ret:
                    rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    h, w, ch = rgb_image.shape
                    bytes_per_line = ch * w
                    qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
                    self.change_pixmap_signal.emit(qt_image)
                else:
                    print("Error: Could not read frame from camera. Retrying...")
                    # Optional: Re-open the capture if it fails
                    self._cap.release()
                    self._cap = cv2.VideoCapture(self._video_url)
                    if not self._cap.isOpened():
                        error_msg = f"Error: Failed to reopen camera at {self._video_url}"
                        print(error_msg)
                        self.stream_error_signal.emit(error_msg)
                        self._running = False
                        break
        except Exception as e:
            error_msg = f'Video capture error: {e}'
            print(error_msg)
            self.stream_error_signal.emit(error_msg)
        finally:
            if self._cap and self._cap.isOpened():
                self._cap.release()
            print("VideoThread finished.")

    def stop(self):
        self._running = False
        self.requestInterruption()
        self.wait() # Wait for the thread to finish execution

    def update_stream_url(self, new_url):
        if self._video_url != new_url:
            print(f"Updating video stream URL from {self._video_url} to {new_url}")
            self.stop() # Stop the current thread
            self._video_url = new_url
            self.start() # Start a new thread with the new URL