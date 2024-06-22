# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sidebar4.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QStatusBar, QTableWidget, QTableWidgetItem, QTextEdit,
    QVBoxLayout, QWidget)
import ressources_rc
import ressources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1364, 833)
        font = QFont()
        font.setBold(True)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.icon_sidebar_wgt = QWidget(self.centralwidget)
        self.icon_sidebar_wgt.setObjectName(u"icon_sidebar_wgt")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.icon_sidebar_wgt.sizePolicy().hasHeightForWidth())
        self.icon_sidebar_wgt.setSizePolicy(sizePolicy)
        self.icon_sidebar_wgt.setStyleSheet(u"QWidget {\n"
"  \n"
"	background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.29052 rgba(0, 152, 0, 255), stop:0.957187 rgba(0, 0, 0, 255));\n"
"}\n"
"\n"
"QPushButton {\n"
"    min-height: 50px;\n"
"    max-height: 50px;\n"
"text-align:left;\n"
"border:none;\n"
"padding-left:10px;\n"
"color:white;\n"
"\n"
"}\n"
"QPushButton:checked{\n"
"background-color: black;\n"
"color: rgb(13, 114, 17);\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.icon_sidebar_wgt)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, 11, -1)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_7 = QLabel(self.icon_sidebar_wgt)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(40, 40))
        self.label_7.setMaximumSize(QSize(40, 40))
        self.label_7.setPixmap(QPixmap(u":/images/new_images/outline_account_circle_black_24dp.png"))
        self.label_7.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_7)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 15, -1, -1)
        self.msg_recus_btn = QPushButton(self.icon_sidebar_wgt)
        self.msg_recus_btn.setObjectName(u"msg_recus_btn")
        self.msg_recus_btn.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/images/new_images/outline_inbox_white_24dp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.msg_recus_btn.setIcon(icon)
        self.msg_recus_btn.setCheckable(True)
        self.msg_recus_btn.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.msg_recus_btn)

        self.msg_create_btn = QPushButton(self.icon_sidebar_wgt)
        self.msg_create_btn.setObjectName(u"msg_create_btn")
        self.msg_create_btn.setStyleSheet(u"color : white;\n"
"text-align:center;")
        icon1 = QIcon()
        icon1.addFile(u":/images/new_images/outline_send_white_24dp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.msg_create_btn.setIcon(icon1)
        self.msg_create_btn.setCheckable(True)
        self.msg_create_btn.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.msg_create_btn)

        self.msg_sent_btn = QPushButton(self.icon_sidebar_wgt)
        self.msg_sent_btn.setObjectName(u"msg_sent_btn")
        self.msg_sent_btn.setStyleSheet(u"color : white;\n"
"text-align:center;")
        icon2 = QIcon()
        icon2.addFile(u":/images/ui_images/messages_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.msg_sent_btn.setIcon(icon2)
        self.msg_sent_btn.setCheckable(True)
        self.msg_sent_btn.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.msg_sent_btn)

        self.msg_orders_btn = QPushButton(self.icon_sidebar_wgt)
        self.msg_orders_btn.setObjectName(u"msg_orders_btn")
        self.msg_orders_btn.setStyleSheet(u"color : white;\n"
"text-align:center;")
        icon3 = QIcon()
        icon3.addFile(u":/images/new_images/outline_shopping_bag_white_24dp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.msg_orders_btn.setIcon(icon3)
        self.msg_orders_btn.setCheckable(True)
        self.msg_orders_btn.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.msg_orders_btn)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 268, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.icon_logout_btn = QPushButton(self.icon_sidebar_wgt)
        self.icon_logout_btn.setObjectName(u"icon_logout_btn")
        self.icon_logout_btn.setStyleSheet(u"color : white;\n"
"text-align:center;")
        icon4 = QIcon()
        icon4.addFile(u":/images/ui_images/log_out_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_logout_btn.setIcon(icon4)

        self.verticalLayout_3.addWidget(self.icon_logout_btn)


        self.gridLayout_3.addWidget(self.icon_sidebar_wgt, 0, 0, 1, 1)

        self.icon_sidebar_wgt_2 = QWidget(self.centralwidget)
        self.icon_sidebar_wgt_2.setObjectName(u"icon_sidebar_wgt_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.icon_sidebar_wgt_2.sizePolicy().hasHeightForWidth())
        self.icon_sidebar_wgt_2.setSizePolicy(sizePolicy1)
        self.icon_sidebar_wgt_2.setStyleSheet(u"QWidget {\n"
"  \n"
"	background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.29052 rgba(0, 152, 0, 255), stop:0.957187 rgba(0, 0, 0, 255));\n"
"}\n"
"\n"
"QPushButton {\n"
"    min-height: 50px;\n"
"    max-height: 50px;\n"
"    text-align: left;\n"
"    border: none;\n"
"    padding-left: 10px;\n"
"    color: white;\n"
"    border-top-left-radius: 10px;  /* Correction de \"border-top-leftr-radius\" */\n"
"    border-bottom-left-radius: 10px;  /* Correction de \"border-bottom-leftr-radius\" */\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: black;\n"
"    color: rgb(0, 255, 0);\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"")
        self.gridLayout = QGridLayout(self.icon_sidebar_wgt_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, 11, -1)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.label_8 = QLabel(self.icon_sidebar_wgt_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(40, 40))
        self.label_8.setMaximumSize(QSize(40, 40))
        self.label_8.setPixmap(QPixmap(u":/images/new_images/outline_account_circle_black_24dp.png"))
        self.label_8.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label_8)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(15)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 15, -1, -1)
        self.big_msg_recus_btn = QPushButton(self.icon_sidebar_wgt_2)
        self.big_msg_recus_btn.setObjectName(u"big_msg_recus_btn")
        self.big_msg_recus_btn.setStyleSheet(u"")
        self.big_msg_recus_btn.setIcon(icon)
        self.big_msg_recus_btn.setCheckable(True)
        self.big_msg_recus_btn.setAutoExclusive(True)

        self.verticalLayout_5.addWidget(self.big_msg_recus_btn)

        self.big_msg_create_btn = QPushButton(self.icon_sidebar_wgt_2)
        self.big_msg_create_btn.setObjectName(u"big_msg_create_btn")
        self.big_msg_create_btn.setStyleSheet(u"")
        self.big_msg_create_btn.setIcon(icon1)
        self.big_msg_create_btn.setCheckable(True)
        self.big_msg_create_btn.setAutoExclusive(True)

        self.verticalLayout_5.addWidget(self.big_msg_create_btn)

        self.big_msg_sent_btn = QPushButton(self.icon_sidebar_wgt_2)
        self.big_msg_sent_btn.setObjectName(u"big_msg_sent_btn")
        self.big_msg_sent_btn.setStyleSheet(u"")
        self.big_msg_sent_btn.setIcon(icon2)
        self.big_msg_sent_btn.setCheckable(True)
        self.big_msg_sent_btn.setAutoExclusive(True)

        self.verticalLayout_5.addWidget(self.big_msg_sent_btn)

        self.big_msg_orders_btn = QPushButton(self.icon_sidebar_wgt_2)
        self.big_msg_orders_btn.setObjectName(u"big_msg_orders_btn")
        self.big_msg_orders_btn.setStyleSheet(u"")
        self.big_msg_orders_btn.setIcon(icon3)
        self.big_msg_orders_btn.setCheckable(True)
        self.big_msg_orders_btn.setAutoExclusive(True)

        self.verticalLayout_5.addWidget(self.big_msg_orders_btn)


        self.gridLayout.addLayout(self.verticalLayout_5, 1, 0, 1, 2)

        self.logout_btn = QPushButton(self.icon_sidebar_wgt_2)
        self.logout_btn.setObjectName(u"logout_btn")
        self.logout_btn.setStyleSheet(u"color : white;\n"
"text-align:center;")
        self.logout_btn.setIcon(icon4)

        self.gridLayout.addWidget(self.logout_btn, 3, 0, 1, 2)

        self.verticalSpacer_3 = QSpacerItem(20, 268, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 2, 1, 1, 1)


        self.gridLayout_3.addWidget(self.icon_sidebar_wgt_2, 0, 1, 1, 1)

        self.main_screen_wdt = QWidget(self.centralwidget)
        self.main_screen_wdt.setObjectName(u"main_screen_wdt")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.main_screen_wdt.sizePolicy().hasHeightForWidth())
        self.main_screen_wdt.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setBold(False)
        self.main_screen_wdt.setFont(font1)
        self.main_screen_wdt.setStyleSheet(u"QWidget {\n"
"  \n"
"	background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.29052 rgba(0, 152, 0, 255), stop:0.957187 rgba(0, 0, 0, 255));\n"
"color:black\n"
"}")
        self.stackedWidget = QStackedWidget(self.main_screen_wdt)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(10, 90, 1000, 701))
        self.stackedWidget.setMaximumSize(QSize(1000, 16777215))
        self.stackedWidget.setFont(font)
        self.stackedWidget.setStyleSheet(u"\n"
"background-color: #F2F2F2;\n"
"color:black;\n"
"\n"
"\n"
"")
        self.ms_recus_page = QWidget()
        self.ms_recus_page.setObjectName(u"ms_recus_page")
        self.ms_recus_page.setFont(font)
        self.label_2 = QLabel(self.ms_recus_page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 10, 211, 67))
        font2 = QFont()
        font2.setFamilies([u"Malgun Gothic"])
        font2.setPointSize(15)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setUnderline(False)
        font2.setKerning(True)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color: rgb(85, 170, 0);")
        self.tableWidget = QTableWidget(self.ms_recus_page)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        icon5 = QIcon()
        icon5.addFile(u":/images/ui_images/image.png", QSize(), QIcon.Normal, QIcon.Off)
        font3 = QFont()
        font3.setFamilies([u"Arial Black"])
        font3.setPointSize(10)
        font3.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font3);
        __qtablewidgetitem.setIcon(icon5);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        icon6 = QIcon()
        icon6.addFile(u":/images/new_images/outline_account_circle_black_24dp.png", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font3);
        __qtablewidgetitem1.setIcon(icon6);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        icon7 = QIcon()
        icon7.addFile(u":/images/new_images/outline_inbox_black_24dp.png", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font3);
        __qtablewidgetitem2.setIcon(icon7);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        icon8 = QIcon()
        icon8.addFile(u":/images/new_images/outline_shopping_bag_black_24dp.png", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font3);
        __qtablewidgetitem3.setIcon(icon8);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(30, 130, 931, 411))
        self.tableWidget.setFont(font)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.stackedWidget.addWidget(self.ms_recus_page)
        self.create_msg_page = QWidget()
        self.create_msg_page.setObjectName(u"create_msg_page")
        self.create_msg_page.setFont(font)
        self.label_3 = QLabel(self.create_msg_page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 20, 211, 67))
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"color: rgb(85, 170, 0);")
        self.layoutWidget = QWidget(self.create_msg_page)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 110, 861, 381))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.layoutWidget)
        self.widget.setObjectName(u"widget")
        self.formLayout = QFormLayout(self.widget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(1)
        self.formLayout.setVerticalSpacing(1)
        self.receiver_mail_le = QLabel(self.widget)
        self.receiver_mail_le.setObjectName(u"receiver_mail_le")
        self.receiver_mail_le.setFont(font3)
        self.receiver_mail_le.setStyleSheet(u"")
        self.receiver_mail_le.setScaledContents(False)
        self.receiver_mail_le.setMargin(10)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.receiver_mail_le)

        self.receiver_mail_la = QLineEdit(self.widget)
        self.receiver_mail_la.setObjectName(u"receiver_mail_la")
        self.receiver_mail_la.setMinimumSize(QSize(0, 40))
        self.receiver_mail_la.setMaximumSize(QSize(750, 40))
        font4 = QFont()
        self.receiver_mail_la.setFont(font4)
        self.receiver_mail_la.setStyleSheet(u"")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.receiver_mail_la)


        self.verticalLayout_4.addWidget(self.widget)

        self.msg_content_txEdit = QTextEdit(self.layoutWidget)
        self.msg_content_txEdit.setObjectName(u"msg_content_txEdit")

        self.verticalLayout_4.addWidget(self.msg_content_txEdit)

        self.send_masg_btn = QPushButton(self.layoutWidget)
        self.send_masg_btn.setObjectName(u"send_masg_btn")
        self.send_masg_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.29052 rgba(0, 152, 0, 255), stop:0.957187 rgba(0, 0, 0, 255));\n"
"    min-height: 50px;\n"
"    max-height: 50px;\n"
"    text-align: center;\n"
"    font-size: 30px;\n"
"    border: 2px solid black; /* Ajout de 'solid black' pour sp\u00e9cifier le style et la couleur de la bordure */\n"
"    color: black;\n"
"    border-top-left-radius: 10px;\n"
"    border-bottom-left-radius: 10px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: black;\n"
"    color: rgb(0, 255, 0);\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"")

        self.verticalLayout_4.addWidget(self.send_masg_btn)

        self.stackedWidget.addWidget(self.create_msg_page)
        self.sent_msg_page = QWidget()
        self.sent_msg_page.setObjectName(u"sent_msg_page")
        self.label_4 = QLabel(self.sent_msg_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 10, 211, 67))
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"color: rgb(85, 170, 0);")
        self.tableWidget_2 = QTableWidget(self.sent_msg_page)
        if (self.tableWidget_2.columnCount() < 4):
            self.tableWidget_2.setColumnCount(4)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font3);
        __qtablewidgetitem4.setIcon(icon5);
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font3);
        __qtablewidgetitem5.setIcon(icon6);
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font3);
        __qtablewidgetitem6.setIcon(icon7);
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font3);
        __qtablewidgetitem7.setIcon(icon8);
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setGeometry(QRect(30, 80, 931, 411))
        self.tableWidget_2.setFont(font)
        self.tableWidget_2.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.stackedWidget.addWidget(self.sent_msg_page)
        self.orders_page = QWidget()
        self.orders_page.setObjectName(u"orders_page")
        self.label_5 = QLabel(self.orders_page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 10, 251, 67))
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"color: rgb(85, 170, 0);")
        self.table = QTableWidget(self.orders_page)
        if (self.table.columnCount() < 8):
            self.table.setColumnCount(8)
        font5 = QFont()
        font5.setPointSize(10)
        font5.setBold(True)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font5);
        self.table.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        font6 = QFont()
        font6.setPointSize(10)
        font6.setBold(True)
        font6.setItalic(False)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font6);
        self.table.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font5);
        self.table.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font5);
        self.table.setHorizontalHeaderItem(3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font5);
        self.table.setHorizontalHeaderItem(4, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFont(font5);
        self.table.setHorizontalHeaderItem(5, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFont(font5);
        self.table.setHorizontalHeaderItem(6, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setFont(font5);
        self.table.setHorizontalHeaderItem(7, __qtablewidgetitem15)
        self.table.setObjectName(u"table")
        self.table.setGeometry(QRect(20, 100, 961, 331))
        self.stackedWidget.addWidget(self.orders_page)
        self.update_order_page = QWidget()
        self.update_order_page.setObjectName(u"update_order_page")
        self.stackedWidget.addWidget(self.update_order_page)
        self.label = QLabel(self.main_screen_wdt)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(190, 30, 331, 41))
        font7 = QFont()
        font7.setPointSize(21)
        font7.setBold(False)
        self.label.setFont(font7)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.main_screen_wdt, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.msg_orders_btn.toggled.connect(self.big_msg_orders_btn.setChecked)
        self.msg_sent_btn.toggled.connect(self.big_msg_sent_btn.setChecked)
        self.msg_create_btn.toggled.connect(self.big_msg_create_btn.setChecked)
        self.msg_recus_btn.toggled.connect(self.big_msg_recus_btn.setChecked)
        self.big_msg_orders_btn.toggled.connect(self.msg_orders_btn.setChecked)
        self.big_msg_sent_btn.toggled.connect(self.msg_sent_btn.setChecked)
        self.big_msg_create_btn.toggled.connect(self.msg_create_btn.setChecked)
        self.big_msg_recus_btn.toggled.connect(self.msg_recus_btn.setChecked)
        self.icon_logout_btn.toggled.connect(MainWindow.close)
        self.logout_btn.toggled.connect(self.statusbar.close)

        self.stackedWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_7.setText("")
        self.msg_recus_btn.setText("")
        self.msg_create_btn.setText("")
        self.msg_sent_btn.setText("")
        self.msg_orders_btn.setText("")
        self.icon_logout_btn.setText("")
        self.label_8.setText("")
        self.big_msg_recus_btn.setText(QCoreApplication.translate("MainWindow", u"MESSAGES RE\u00c7US     ", None))
        self.big_msg_create_btn.setText(QCoreApplication.translate("MainWindow", u"CR\u00c9ER UN MESSAGE  ", None))
        self.big_msg_sent_btn.setText(QCoreApplication.translate("MainWindow", u"MESSAGES ENVOY\u00c9S", None))
        self.big_msg_orders_btn.setText(QCoreApplication.translate("MainWindow", u"COMMANDES", None))
        self.logout_btn.setText(QCoreApplication.translate("MainWindow", u"SE DECONNECTER", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Messages recus", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"De :", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"A :", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Date :", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Message", None));
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Envoyer message", None))
        self.receiver_mail_le.setText(QCoreApplication.translate("MainWindow", u"To :", None))
        self.receiver_mail_la.setText("")
        self.send_masg_btn.setText(QCoreApplication.translate("MainWindow", u"Envoyer", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Messages envoy\u00e9s", None))
        ___qtablewidgetitem4 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"De :", None));
        ___qtablewidgetitem5 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"A :", None));
        ___qtablewidgetitem6 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Date :", None));
        ___qtablewidgetitem7 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Message", None));
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Articles command\u00e9s", None))
        ___qtablewidgetitem8 = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"ID de la commande", None));
        ___qtablewidgetitem9 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Quantit\u00e9", None));
        ___qtablewidgetitem10 = self.table.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Produit", None));
        ___qtablewidgetitem11 = self.table.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Prix unitaire", None));
        ___qtablewidgetitem12 = self.table.horizontalHeaderItem(4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Statut", None));
        ___qtablewidgetitem13 = self.table.horizontalHeaderItem(5)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Soci\u00e9t\u00e9", None));
        ___qtablewidgetitem14 = self.table.horizontalHeaderItem(6)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Client", None));
        ___qtablewidgetitem15 = self.table.horizontalHeaderItem(7)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Commentaire", None));
        self.label.setText(QCoreApplication.translate("MainWindow", u"VENTALIS", None))
    # retranslateUi

