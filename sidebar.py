from PySide6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from ui_sidebar import Ui_MainWindow
from api_session import LoginSession

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

        # Connexion pour la page de création de messages
        self.send_masg_btn.clicked.connect(self.send_message)

    # Méthodes pour basculer entre les pages
    def switch_to_received_msg_page(self):
        self.stackedWidget.setCurrentIndex(0)
        self.load_received_messages()

    def switch_to_create_msg_page(self):
        self.stackedWidget.setCurrentIndex(1)

    def switch_to_sentmsg_page(self):
        self.stackedWidget.setCurrentIndex(2)
        self.load_sent_messages()

    def switch_orders_page(self):
        self.stackedWidget.setCurrentIndex(3)
        self.load_order_items()

    def switch_to_update_order_page(self):
        self.stackedWidget.setCurrentIndex(4)

    # Méthode pour envoyer un message
    def send_message(self):
        receiver_email = self.receiver_mail_la.text()
        content = self.msg_content_txEdit.toPlainText()
        try:
            message_response = self.login_session.create_message(receiver_email, content)
            QMessageBox.information(self, 'Message Sent', f'Message to {receiver_email} sent successfully.')
            print(message_response)
            # Nettoyer les champs de saisie après l'envoi
            self.receiver_mail_la.clear()
            self.msg_content_txEdit.clear()
        except Exception as e:
            QMessageBox.warning(self, 'Message Failed', str(e))

    # Méthode pour récupérer les messages reçus
    def load_sent_messages(self):
        try:
            messages = self.login_session.get_sent_messages()
            print("Sent messages:", messages)  # Debug: print messages

            # Assurez-vous que la table est correctement référencée
            if not hasattr(self, 'tableWidget_2'):
                print("Error: 'tableWidget_2' is not defined in self")
                return

            # Configuration des en-têtes de colonnes
            self.tableWidget_2.setColumnCount(4)
            self.tableWidget_2.setHorizontalHeaderLabels(['ID', 'Receiver Email', 'Content', 'Date'])

            self.tableWidget_2.setRowCount(len(messages))
            for row_num, message in enumerate(messages):
                print("Adding sent message:", message)  # Debug: print each message
                self.tableWidget_2.setItem(row_num, 0, QTableWidgetItem(str(message['id'])))
                self.tableWidget_2.setItem(row_num, 1, QTableWidgetItem(message['receiver_email']))
                self.tableWidget_2.setItem(row_num, 2, QTableWidgetItem(message['content']))
                self.tableWidget_2.setItem(row_num, 3, QTableWidgetItem(message['timestamp']))

            # Ajuster la largeur des colonnes en fonction du contenu
            self.tableWidget_2.resizeColumnsToContents()
        except Exception as e:
            QMessageBox.warning(self, 'Failed to Load Sent Messages', str(e))

            # Méthode pour récupérer les messages reçus
    def load_received_messages(self):
        try:
            messages = self.login_session.get_the_messages()
            print("Messages received:", messages)  # Debug: print messages

            # Configuration des en-têtes de colonnes
            self.tableWidget.setColumnCount(4)
            self.tableWidget.setHorizontalHeaderLabels(['ID', 'Sender Email', 'Content', 'Date'])

            self.tableWidget.setRowCount(len(messages))
            for row_num, message in enumerate(messages):
                print("Adding message:", message)  # Debug: print each message
                self.tableWidget.setItem(row_num, 0, QTableWidgetItem(str(message['id'])))
                self.tableWidget.setItem(row_num, 1, QTableWidgetItem(message['sender_email']))
                self.tableWidget.setItem(row_num, 2, QTableWidgetItem(message['content']))
                self.tableWidget.setItem(row_num, 3, QTableWidgetItem(message['timestamp']))

            # Ajuster la largeur des colonnes en fonction du contenu
            self.tableWidget.resizeColumnsToContents()
        except Exception as e:
            QMessageBox.warning(self, 'Failed to Load Messages', str(e))

    # Méthode pour charger les commandes
    def load_order_items(self):
        try:
            orders = self.login_session.get_order_items()
            print("Order items:", orders)  # Debug: print orders

            # Assurez-vous que la table est correctement référencée
            if not hasattr(self, 'table'):
                print("Error: 'table' is not defined in self")
                return

            # Configuration des en-têtes de colonnes
            self.table.setColumnCount(8)
            self.table.setHorizontalHeaderLabels(
                ['Order ID', 'Product Name', 'Customer Email', 'Status', 'Quantity', 'Comment', 'Date Added',
                 'Order Number'])

            self.table.setRowCount(len(orders))
            for row_num, order in enumerate(orders):
                print("Adding order:", order)  # Debug: print each order
                self.table.setItem(row_num, 0, QTableWidgetItem(str(order['id'])))
                self.table.setItem(row_num, 1, QTableWidgetItem(order['product']['name']))
                self.table.setItem(row_num, 2, QTableWidgetItem(order['customer']['email']))
                self.table.setItem(row_num, 3, QTableWidgetItem(order['status']))
                self.table.setItem(row_num, 4, QTableWidgetItem(str(order['quantity'])))
                self.table.setItem(row_num, 5, QTableWidgetItem(order['comment'] or ''))
                self.table.setItem(row_num, 6, QTableWidgetItem(order['date_added']))
                self.table.setItem(row_num, 7, QTableWidgetItem(str(order['order'])))

            # Ajuster la largeur des colonnes en fonction du contenu
            self.table.resizeColumnsToContents()
        except Exception as e:
            QMessageBox.warning(self, 'Failed to Load Orders', str(e))