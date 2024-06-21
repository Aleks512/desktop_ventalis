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
        MainWindow.resize(1368, 841)
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

        self.msg_update_btn = QPushButton(self.icon_sidebar_wgt)
        self.msg_update_btn.setObjectName(u"msg_update_btn")
        self.msg_update_btn.setStyleSheet(u"color : white;\n"
"text-align:center;")
        icon4 = QIcon()
        icon4.addFile(u":/images/ui_images/notifications_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.msg_update_btn.setIcon(icon4)
        self.msg_update_btn.setCheckable(True)
        self.msg_update_btn.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.msg_update_btn)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 268, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.msg_sent_btn_11 = QPushButton(self.icon_sidebar_wgt)
        self.msg_sent_btn_11.setObjectName(u"msg_sent_btn_11")
        self.msg_sent_btn_11.setStyleSheet(u"color : white;\n"
"text-align:center;")
        icon5 = QIcon()
        icon5.addFile(u":/images/ui_images/log_out_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.msg_sent_btn_11.setIcon(icon5)

        self.verticalLayout_3.addWidget(self.msg_sent_btn_11)


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

        self.big_msg_update_btn = QPushButton(self.icon_sidebar_wgt_2)
        self.big_msg_update_btn.setObjectName(u"big_msg_update_btn")
        self.big_msg_update_btn.setStyleSheet(u"")
        self.big_msg_update_btn.setIcon(icon4)
        self.big_msg_update_btn.setCheckable(True)
        self.big_msg_update_btn.setAutoExclusive(True)

        self.verticalLayout_5.addWidget(self.big_msg_update_btn)


        self.gridLayout.addLayout(self.verticalLayout_5, 1, 0, 1, 2)

        self.msg_sent_btn_16 = QPushButton(self.icon_sidebar_wgt_2)
        self.msg_sent_btn_16.setObjectName(u"msg_sent_btn_16")
        self.msg_sent_btn_16.setStyleSheet(u"color : white;\n"
"text-align:center;")
        self.msg_sent_btn_16.setIcon(icon5)

        self.gridLayout.addWidget(self.msg_sent_btn_16, 3, 0, 1, 2)

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
        self.header = QWidget(self.main_screen_wdt)
        self.header.setObjectName(u"header")
        self.header.setGeometry(QRect(10, 20, 1001, 53))
        self.header.setStyleSheet(u"background-color: #F2F2F2;")
        self.verticalLayout_2 = QVBoxLayout(self.header)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.menu_btn = QPushButton(self.header)
        self.menu_btn.setObjectName(u"menu_btn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.menu_btn.sizePolicy().hasHeightForWidth())
        self.menu_btn.setSizePolicy(sizePolicy3)
        self.menu_btn.setMinimumSize(QSize(40, 0))
        self.menu_btn.setMaximumSize(QSize(40, 16777215))
        icon6 = QIcon()
        icon6.addFile(u":/images/ui_images/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_btn.setIcon(icon6)
        self.menu_btn.setCheckable(True)
        self.menu_btn.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.menu_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.search_lineEdit = QLineEdit(self.header)
        self.search_lineEdit.setObjectName(u"search_lineEdit")
        self.search_lineEdit.setMinimumSize(QSize(250, 0))
        self.search_lineEdit.setMaximumSize(QSize(250, 16777215))

        self.horizontalLayout_2.addWidget(self.search_lineEdit)

        self.search_btn = QPushButton(self.header)
        self.search_btn.setObjectName(u"search_btn")
        self.search_btn.setMinimumSize(QSize(40, 0))
        self.search_btn.setMaximumSize(QSize(40, 16777215))
        icon7 = QIcon()
        icon7.addFile(u":/images/ui_images/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.search_btn.setIcon(icon7)

        self.horizontalLayout_2.addWidget(self.search_btn)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.pushButton_16 = QPushButton(self.header)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setMinimumSize(QSize(40, 0))
        self.pushButton_16.setMaximumSize(QSize(40, 16777215))
        icon8 = QIcon()
        icon8.addFile(u":/images/ui_images/image.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_16.setIcon(icon8)

        self.horizontalLayout_2.addWidget(self.pushButton_16)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

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
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        font3 = QFont()
        font3.setFamilies([u"Arial Black"])
        font3.setPointSize(10)
        font3.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font3);
        __qtablewidgetitem.setIcon(icon8);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        icon9 = QIcon()
        icon9.addFile(u":/images/new_images/outline_account_circle_black_24dp.png", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font3);
        __qtablewidgetitem1.setIcon(icon9);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        icon10 = QIcon()
        icon10.addFile(u":/images/new_images/outline_inbox_black_24dp.png", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font3);
        __qtablewidgetitem2.setIcon(icon10);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        icon11 = QIcon()
        icon11.addFile(u":/images/new_images/outline_shopping_bag_black_24dp.png", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font3);
        __qtablewidgetitem3.setIcon(icon11);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        icon12 = QIcon()
        icon12.addFile(u":/images/new_images/outline_send_black_24dp.png", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font3);
        __qtablewidgetitem4.setIcon(icon12);
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
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
        if (self.tableWidget_2.columnCount() < 5):
            self.tableWidget_2.setColumnCount(5)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font3);
        __qtablewidgetitem5.setIcon(icon8);
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font3);
        __qtablewidgetitem6.setIcon(icon9);
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font3);
        __qtablewidgetitem7.setIcon(icon10);
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font3);
        __qtablewidgetitem8.setIcon(icon11);
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font3);
        __qtablewidgetitem9.setIcon(icon12);
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem9)
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
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font5);
        self.table.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        font6 = QFont()
        font6.setPointSize(10)
        font6.setBold(True)
        font6.setItalic(False)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font6);
        self.table.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font5);
        self.table.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFont(font5);
        self.table.setHorizontalHeaderItem(3, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFont(font5);
        self.table.setHorizontalHeaderItem(4, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setFont(font5);
        self.table.setHorizontalHeaderItem(5, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setFont(font5);
        self.table.setHorizontalHeaderItem(6, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setFont(font5);
        self.table.setHorizontalHeaderItem(7, __qtablewidgetitem17)
        self.table.setObjectName(u"table")
        self.table.setGeometry(QRect(20, 100, 961, 331))
        self.stackedWidget.addWidget(self.orders_page)
        self.update_order_page = QWidget()
        self.update_order_page.setObjectName(u"update_order_page")
        self.label_6 = QLabel(self.update_order_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 10, 411, 67))
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"color: rgb(85, 170, 0);")
        self.stackedWidget.addWidget(self.update_order_page)

        self.gridLayout_3.addWidget(self.main_screen_wdt, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.menu_btn.toggled.connect(self.icon_sidebar_wgt.setHidden)
        self.menu_btn.toggled.connect(self.icon_sidebar_wgt_2.setVisible)
        self.msg_update_btn.toggled.connect(self.big_msg_update_btn.setChecked)
        self.msg_orders_btn.toggled.connect(self.big_msg_orders_btn.setChecked)
        self.msg_sent_btn.toggled.connect(self.big_msg_sent_btn.setChecked)
        self.msg_create_btn.toggled.connect(self.big_msg_create_btn.setChecked)
        self.msg_recus_btn.toggled.connect(self.big_msg_recus_btn.setChecked)
        self.big_msg_update_btn.toggled.connect(self.msg_update_btn.setChecked)
        self.big_msg_orders_btn.toggled.connect(self.msg_orders_btn.setChecked)
        self.big_msg_sent_btn.toggled.connect(self.msg_sent_btn.setChecked)
        self.big_msg_create_btn.toggled.connect(self.msg_create_btn.setChecked)
        self.big_msg_recus_btn.toggled.connect(self.msg_recus_btn.setChecked)
        self.msg_sent_btn_11.toggled.connect(MainWindow.close)
        self.msg_sent_btn_16.toggled.connect(self.statusbar.close)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_7.setText("")
        self.msg_recus_btn.setText("")
        self.msg_create_btn.setText("")
        self.msg_sent_btn.setText("")
        self.msg_orders_btn.setText("")
        self.msg_update_btn.setText("")
        self.msg_sent_btn_11.setText("")
        self.label_8.setText("")
        self.big_msg_recus_btn.setText(QCoreApplication.translate("MainWindow", u"MESSAGES RE\u00c7US     ", None))
        self.big_msg_create_btn.setText(QCoreApplication.translate("MainWindow", u"CR\u00c9ER UN MESSAGE  ", None))
        self.big_msg_sent_btn.setText(QCoreApplication.translate("MainWindow", u"MESSAGES ENVOY\u00c9S", None))
        self.big_msg_orders_btn.setText(QCoreApplication.translate("MainWindow", u"COMMANDES", None))
        self.big_msg_update_btn.setText(QCoreApplication.translate("MainWindow", u"MISE A JOUR", None))
        self.msg_sent_btn_16.setText(QCoreApplication.translate("MainWindow", u"SE DECONNECTER", None))
        self.menu_btn.setText("")
        self.search_btn.setText("")
        self.pushButton_16.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Messages recus", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"De :", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"A :", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Date :", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Message", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"R\u00e9pondre :", None));
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Envoyer message", None))
        self.receiver_mail_le.setText(QCoreApplication.translate("MainWindow", u"To :", None))
        self.receiver_mail_la.setText("")
        self.send_masg_btn.setText(QCoreApplication.translate("MainWindow", u"Envoyer", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Messages envoy\u00e9s", None))
        ___qtablewidgetitem5 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"De :", None));
        ___qtablewidgetitem6 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"A :", None));
        ___qtablewidgetitem7 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Date :", None));
        ___qtablewidgetitem8 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Message", None));
        ___qtablewidgetitem9 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"R\u00e9pondre :", None));
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Articles command\u00e9s", None))
        ___qtablewidgetitem10 = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"ID de la commande", None));
        ___qtablewidgetitem11 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Quantit\u00e9", None));
        ___qtablewidgetitem12 = self.table.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Produit", None));
        ___qtablewidgetitem13 = self.table.horizontalHeaderItem(3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Prix unitaire", None));
        ___qtablewidgetitem14 = self.table.horizontalHeaderItem(4)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Statut", None));
        ___qtablewidgetitem15 = self.table.horizontalHeaderItem(5)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Soci\u00e9t\u00e9", None));
        ___qtablewidgetitem16 = self.table.horizontalHeaderItem(6)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Client", None));
        ___qtablewidgetitem17 = self.table.horizontalHeaderItem(7)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Commentaire", None));
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Changer le status de la commande", None))
    # retranslateUi

