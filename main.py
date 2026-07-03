import sys
from PySide6.QtWidgets import QApplication
from src.gui.main_window import DroneMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DroneMainWindow()
    window.show()
    sys.exit(app.exec())
