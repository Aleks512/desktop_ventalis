from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PySide6.QtGui import QIcon  # Import correct pour QIcon
from PySide6.QtCore import QSize

class Sidebar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUI()

    def setupUI(self):
        self.layout = QVBoxLayout(self)
        self.menu_btn = QPushButton("Menu")
        self.menu_btn.setCheckable(True)
        self.layout.addWidget(self.menu_btn)

        # Ajout de boutons avec des icônes spécifiques et styles
        self.addButton("Messages Reçus", ":/images/new_images/outline_inbox_white_24dp.png")
        self.addButton("Créer Message", ":/images/new_images/outline_send_white_24dp.png")
        self.addButton("Messages Envoyés", ":/images/ui_images/messages_white.png")
        self.addButton("Commandes", ":/images/new_images/outline_shopping_bag_white_24dp.png")
        self.addButton("Mises à jour", ":/images/ui_images/notifications_white.png")

    def addButton(self, text, icon_path):
        button = QPushButton(text)
        button.setIcon(QIcon(icon_path))
        button.setCheckable(True)
        button.setAutoExclusive(True)
        self.layout.addWidget(button)
