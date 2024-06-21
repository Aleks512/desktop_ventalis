from PySide6.QtWidgets import QMainWindow
from ui_sidebar import Ui_MainWindow

class Sidebar(QMainWindow, Ui_MainWindow):
    def __init__(self, login_session):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Ventalis - Main Window")
        self.login_session = login_session  # Stocke l'instance de la session de connexion

        # Cache l'icône de la barre latérale au début
        self.icon_sidebar_wgt.setHidden(True)

        # Connexions des boutons aux méthodes appropriées
        self.big_msg_recus_btn.clicked.connect(self.switch_to_received_msg_page)
        self.msg_recus_btn.clicked.connect(self.switch_to_received_msg_page)

        self.big_msg_create_btn.clicked.connect(self.switch_to_create_msg_page)
        self.msg_create_btn.clicked.connect(self.switch_to_create_msg_page)

        self.big_msg_sent_btn.clicked.connect(self.switch_to_sentmsg_page)
        self.msg_sent_btn.clicked.connect(self.switch_to_sentmsg_page)

        self.big_msg_orders_btn.clicked.connect(self.switch_orders_page)
        self.msg_orders_btn.clicked.connect(self.switch_orders_page)

        self.big_msg_update_btn.clicked.connect(self.switch_to_update_order_page)
        #self.update_order_btn.clicked.connect(self.switch_to_update_order_page)

    # Méthodes pour basculer entre les pages
    def switch_to_received_msg_page(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_create_msg_page(self):
        self.stackedWidget.setCurrentIndex(1)

    def switch_to_sentmsg_page(self):
        self.stackedWidget.setCurrentIndex(2)

    def switch_orders_page(self):
        self.stackedWidget.setCurrentIndex(3)

    def switch_to_update_order_page(self):
        self.stackedWidget.setCurrentIndex(4)
