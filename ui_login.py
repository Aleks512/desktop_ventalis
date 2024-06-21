# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1200, 800)
        self.bg_widget = QWidget(Dialog)
        self.bg_widget.setObjectName(u"bg_widget")
        self.bg_widget.setGeometry(QRect(-20, 10, 1200, 800))
        self.bg_widget.setStyleSheet(u"QWidget#bg_widget{\n"
"background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.29052 rgba(0, 152, 0, 255), stop:0.957187 rgba(0, 0, 0, 255));}")
        self.ventalis_title = QLabel(self.bg_widget)
        self.ventalis_title.setObjectName(u"ventalis_title")
        self.ventalis_title.setGeometry(QRect(480, 180, 281, 50))
        self.ventalis_title.setAutoFillBackground(False)
        self.ventalis_title.setStyleSheet(u"font: 75 36pt \"Century Schoolbook\"; color :rgb(0, 0, 0);\n"
"font: 36pt \"Sylfaen\";")
        self.soustitle = QLabel(self.bg_widget)
        self.soustitle.setObjectName(u"soustitle")
        self.soustitle.setGeometry(QRect(520, 240, 171, 81))
        self.soustitle.setAutoFillBackground(False)
        self.soustitle.setStyleSheet(u"font: 75 36pt \"Century Schoolbook\"; color :rgb(0, 0, 0);\n"
"font: 22pt \"Sylfaen\";")
        self.formLayoutWidget = QWidget(self.bg_widget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(490, 320, 275, 151))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.email_label = QLabel(self.formLayoutWidget)
        self.email_label.setObjectName(u"email_label")
        self.email_label.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.email_label)

        self.pwd_label = QLabel(self.formLayoutWidget)
        self.pwd_label.setObjectName(u"pwd_label")
        self.pwd_label.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.pwd_label)

        self.pwd_input = QLineEdit(self.formLayoutWidget)
        self.pwd_input.setObjectName(u"pwd_input")
        self.pwd_input.setStyleSheet(u"background-color : rgba(0,0,0,0);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(0,255, 0);  /* Exemple : bordure verte */")

        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.pwd_input)

        self.email_input = QLineEdit(self.formLayoutWidget)
        self.email_input.setObjectName(u"email_input")
        self.email_input.setStyleSheet(u"background-color : rgba(0,0,0,0);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(0,255, 0);  /* Exemple : bordure verte */\n"
"")

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.email_input)

        self.email_error = QLabel(self.formLayoutWidget)
        self.email_error.setObjectName(u"email_error")
        self.email_error.setStyleSheet(u"font: 9pt \"MS Shell Dlg 2\";\n"
"color:red;")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.email_error)

        self.pwd_error = QLabel(self.formLayoutWidget)
        self.pwd_error.setObjectName(u"pwd_error")
        self.pwd_error.setStyleSheet(u"color: red;\n"
"font: 9pt \"MS Shell Dlg 2\";")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.pwd_error)

        self.connexion_btn = QPushButton(self.bg_widget)
        self.connexion_btn.setObjectName(u"connexion_btn")
        self.connexion_btn.setGeometry(QRect(490, 510, 251, 61))
        self.connexion_btn.setStyleSheet(u"color : rgb(0, 255, 0);\n"
"background-color: black;\n"
"\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"border-color: white;\n"
"border-style: solid;\n"
"border-style: solid;\n"
"border-radius: 30px;")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"welcomescreen", None))
        self.ventalis_title.setText(QCoreApplication.translate("Dialog", u"VENTALIS", None))
        self.soustitle.setText(QCoreApplication.translate("Dialog", u"Connexion", None))
        self.email_label.setText(QCoreApplication.translate("Dialog", u"Email", None))
        self.pwd_label.setText(QCoreApplication.translate("Dialog", u"Mot de passe", None))
        self.email_error.setText("")
        self.pwd_error.setText("")
        self.connexion_btn.setText(QCoreApplication.translate("Dialog", u"Se connecter", None))
    # retranslateUi

