# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'drone_interface.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_DroneInterface(object):
    def setupUi(self, DroneInterface):
        if not DroneInterface.objectName():
            DroneInterface.setObjectName(u"DroneInterface")
        DroneInterface.resize(800, 600)
        self.main_layout = QVBoxLayout(DroneInterface)
        self.main_layout.setObjectName(u"main_layout")
        self.video_label = QLabel(DroneInterface)
        self.video_label.setObjectName(u"video_label")
        self.video_label.setAlignment(Qt.AlignCenter)

        self.main_layout.addWidget(self.video_label)

        self.control_buttons_layout = QGridLayout()
        self.control_buttons_layout.setObjectName(u"control_buttons_layout")
        self.btn_up = QPushButton(DroneInterface)
        self.btn_up.setObjectName(u"btn_up")

        self.control_buttons_layout.addWidget(self.btn_up, 0, 1, 1, 1)

        self.btn_turn_left = QPushButton(DroneInterface)
        self.btn_turn_left.setObjectName(u"btn_turn_left")

        self.control_buttons_layout.addWidget(self.btn_turn_left, 1, 0, 1, 1)

        self.btn_turn_right = QPushButton(DroneInterface)
        self.btn_turn_right.setObjectName(u"btn_turn_right")

        self.control_buttons_layout.addWidget(self.btn_turn_right, 1, 2, 1, 1)

        self.btn_down = QPushButton(DroneInterface)
        self.btn_down.setObjectName(u"btn_down")

        self.control_buttons_layout.addWidget(self.btn_down, 2, 1, 1, 1)

        self.btn_forward = QPushButton(DroneInterface)
        self.btn_forward.setObjectName(u"btn_forward")

        self.control_buttons_layout.addWidget(self.btn_forward, 0, 4, 1, 1)

        self.btn_strafe_left = QPushButton(DroneInterface)
        self.btn_strafe_left.setObjectName(u"btn_strafe_left")

        self.control_buttons_layout.addWidget(self.btn_strafe_left, 1, 3, 1, 1)

        self.btn_strafe_right = QPushButton(DroneInterface)
        self.btn_strafe_right.setObjectName(u"btn_strafe_right")

        self.control_buttons_layout.addWidget(self.btn_strafe_right, 1, 5, 1, 1)

        self.btn_backward = QPushButton(DroneInterface)
        self.btn_backward.setObjectName(u"btn_backward")

        self.control_buttons_layout.addWidget(self.btn_backward, 2, 4, 1, 1)


        self.main_layout.addLayout(self.control_buttons_layout)

        self.action_buttons_layout = QGridLayout()
        self.action_buttons_layout.setObjectName(u"action_buttons_layout")
        self.btn_land = QPushButton(DroneInterface)
        self.btn_land.setObjectName(u"btn_land")

        self.action_buttons_layout.addWidget(self.btn_land, 0, 0, 1, 1)

        self.btn_takeoff = QPushButton(DroneInterface)
        self.btn_takeoff.setObjectName(u"btn_takeoff")

        self.action_buttons_layout.addWidget(self.btn_takeoff, 0, 1, 1, 1)


        self.main_layout.addLayout(self.action_buttons_layout)

        self.line = QFrame(DroneInterface)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.main_layout.addWidget(self.line)

        self.groupBox_connection_settings = QGroupBox(DroneInterface)
        self.groupBox_connection_settings.setObjectName(u"groupBox_connection_settings")
        self.connection_settings_layout = QGridLayout(self.groupBox_connection_settings)
        self.connection_settings_layout.setObjectName(u"connection_settings_layout")
        self.label_drone_ip = QLabel(self.groupBox_connection_settings)
        self.label_drone_ip.setObjectName(u"label_drone_ip")

        self.connection_settings_layout.addWidget(self.label_drone_ip, 0, 0, 1, 1)

        self.le_drone_ip = QLineEdit(self.groupBox_connection_settings)
        self.le_drone_ip.setObjectName(u"le_drone_ip")

        self.connection_settings_layout.addWidget(self.le_drone_ip, 0, 1, 1, 1)

        self.label_drone_port = QLabel(self.groupBox_connection_settings)
        self.label_drone_port.setObjectName(u"label_drone_port")

        self.connection_settings_layout.addWidget(self.label_drone_port, 1, 0, 1, 1)

        self.le_drone_port = QLineEdit(self.groupBox_connection_settings)
        self.le_drone_port.setObjectName(u"le_drone_port")

        self.connection_settings_layout.addWidget(self.le_drone_port, 1, 1, 1, 1)

        self.label_video_url = QLabel(self.groupBox_connection_settings)
        self.label_video_url.setObjectName(u"label_video_url")

        self.connection_settings_layout.addWidget(self.label_video_url, 2, 0, 1, 1)

        self.le_video_url = QLineEdit(self.groupBox_connection_settings)
        self.le_video_url.setObjectName(u"le_video_url")

        self.connection_settings_layout.addWidget(self.le_video_url, 2, 1, 1, 1)

        self.btn_apply_settings = QPushButton(self.groupBox_connection_settings)
        self.btn_apply_settings.setObjectName(u"btn_apply_settings")

        self.connection_settings_layout.addWidget(self.btn_apply_settings, 3, 1, 1, 1)


        self.main_layout.addWidget(self.groupBox_connection_settings)


        self.retranslateUi(DroneInterface)

        QMetaObject.connectSlotsByName(DroneInterface)
    # setupUi

    def retranslateUi(self, DroneInterface):
        DroneInterface.setWindowTitle(QCoreApplication.translate("DroneInterface", u"MiniDrone Remote Controller", None))
        self.video_label.setText(QCoreApplication.translate("DroneInterface", u"No Video Feed", None))
        self.btn_up.setText(QCoreApplication.translate("DroneInterface", u"Up (W)", None))
        self.btn_turn_left.setText(QCoreApplication.translate("DroneInterface", u"Turn Left (A)", None))
        self.btn_turn_right.setText(QCoreApplication.translate("DroneInterface", u"Turn Right (D)", None))
        self.btn_down.setText(QCoreApplication.translate("DroneInterface", u"Down (S)", None))
        self.btn_forward.setText(QCoreApplication.translate("DroneInterface", u"Forward (I)", None))
        self.btn_strafe_left.setText(QCoreApplication.translate("DroneInterface", u"Left (J)", None))
        self.btn_strafe_right.setText(QCoreApplication.translate("DroneInterface", u"Right (L)", None))
        self.btn_backward.setText(QCoreApplication.translate("DroneInterface", u"Backward (K)", None))
        self.btn_land.setText(QCoreApplication.translate("DroneInterface", u"Landing (Esc)", None))
        self.btn_takeoff.setText(QCoreApplication.translate("DroneInterface", u"Take Off (Backspace)", None))
        self.groupBox_connection_settings.setTitle(QCoreApplication.translate("DroneInterface", u"Connection Settings", None))
        self.label_drone_ip.setText(QCoreApplication.translate("DroneInterface", u"Drone IP:", None))
        self.label_drone_port.setText(QCoreApplication.translate("DroneInterface", u"Drone Port:", None))
        self.label_video_url.setText(QCoreApplication.translate("DroneInterface", u"Video URL:", None))
        self.btn_apply_settings.setText(QCoreApplication.translate("DroneInterface", u"Apply Settings", None))
    # retranslateUi

