from sidebar import (Ui_MainWindow)
from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QVBoxLayout, QWidget


class Sidebar(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Ventalis - Main Window")

        self.icon_sidebar_wgt.setHidden(True)


        self.big_msg_recus_btn.clicked.connect(self.swith_to_received_msg_page)
        self.msg_recus_btn.clicked.connect(self.swith_to_received_msg_page)

        self.big_msg_create_btn.clicked.connect(self.swith_to_create_msg_page)
        self.msg_create_btn.clicked.connect(self.swith_to_create_msg_page)

        self.big_msg_sent_btn.clicked.connect(self.swith_to_sentmsg_page)
        self.msg_sent_btn.clicked.connect(self.swith_to_sentmsg_page)

        self.big_msg_orders_btn.clicked.connect(self.swith_orders_page)
        self.msg_orders_btn.clicked.connect(self.swith_orders_page)

        self.big_msg_update_btn.clicked.connect(self.swith_to_update_order_page)
        #self.update_order_btn.clicked.connect(self.swith_to_update_order_page)


#1. Define the methods to switch between pages
    def swith_to_received_msg_page(self):
        self.stackedWidget.setCurrentIndex(0)

    def swith_to_create_msg_page(self):
        self.stackedWidget.setCurrentIndex(1)

    def swith_to_sentmsg_page(self):
        self.stackedWidget.setCurrentIndex(2)

    def swith_orders_page(self):
        self.stackedWidget.setCurrentIndex(3)

    def swith_to_update_order_page(self):
        self.stackedWidget.setCurrentIndex(4)