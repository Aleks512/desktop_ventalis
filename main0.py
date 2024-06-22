import sys
from PySide6.QtWidgets import QApplication, QDialog, QStackedWidget
from ui_welcomescreen import Ui_welcome
from login import LoginScreen
from sidebar import Sidebar

class WelcomeScreen(QDialog):
    def __init__(self, widget):
        super().__init__()
        self.ui = Ui_welcome() # Crée une instance de la classe Ui_welcome, produit de la conversion de welcome.ui
        self.ui.setupUi(self) # Configure l'interface utilisateur pour l'objet QDialog actuel
        self.setWindowTitle('Ventalis - Bienvenue') # Définit le titre de la fenêtre
        self.widget = widget # Référence à l'objet QStackedWidget
        self.ui.login.clicked.connect(self.gotologin) # Connecte le signal clicked du bouton login à la méthode gotologin

    def gotologin(self):
        # Si l'écran de login n'a pas encore été ajouté, on l'ajoute.
        if self.widget.count() == 1:  # Il n'y a que WelcomeScreen dans le stack
            login_screen = LoginScreen(self.widget) # Crée une instance de la classe LoginScreen
            self.widget.addWidget(login_screen) # Ajoute l'écran de connexion au QStackedWidget
        self.widget.setCurrentIndex(1)  # Passe à l'écran de connexion

if __name__ == '__main__':
    app = QApplication(sys.argv) # Crée une instance de QApplication
    widget = QStackedWidget() # Crée une instance de QStackedWidget

    welcome_screen = WelcomeScreen(widget) # Crée une instance de la classe WelcomeScreen
    widget.addWidget(welcome_screen)    # Ajoute l'écran d'accueil au QStackedWidget

    # Assure que la fenêtre principale ait des dimensions fixes et appropriées
    widget.setFixedWidth(1200)
    widget.setFixedHeight(800)
    widget.show()
    sys.exit(app.exec())
