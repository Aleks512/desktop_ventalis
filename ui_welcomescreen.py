# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'welcomescreen.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_welcome(object):
    def setupUi(self, welcome):
        if not welcome.objectName():
            welcome.setObjectName(u"welcome")
        welcome.resize(1112, 800)
        self.bg_widget = QWidget(welcome)
        self.bg_widget.setObjectName(u"bg_widget")
        self.bg_widget.setGeometry(QRect(-40, 10, 1200, 800))
        self.bg_widget.setStyleSheet(u"QWidget#bg_widget{\n"
"background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.29052 rgba(0, 152, 0, 255), stop:0.957187 rgba(0, 0, 0, 255));}")
        self.label = QLabel(self.bg_widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(480, 340, 281, 50))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"font: 75 36pt \"Century Schoolbook\"; color :rgb(0, 0, 0);\n"
"font: 36pt \"Sylfaen\";")
        self.login = QPushButton(self.bg_widget)
        self.login.setObjectName(u"login")
        self.login.setGeometry(QRect(470, 410, 281, 61))
        self.login.setStyleSheet(u"color : rgb(0, 255, 0);\n"
"background-color: black;\n"
"\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"border-color: white;\n"
"border-style: solid;\n"
"border-style: solid;\n"
"border-radius: 30px;")

        self.retranslateUi(welcome)

        QMetaObject.connectSlotsByName(welcome)
    # setupUi

    def retranslateUi(self, welcome):
        welcome.setWindowTitle(QCoreApplication.translate("welcome", u"welcomescreen", None))
        self.label.setText(QCoreApplication.translate("welcome", u"VENTALIS", None))
        self.login.setText(QCoreApplication.translate("welcome", u"Connexion", None))
    # retranslateUi

