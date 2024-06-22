from PySide6.QtWidgets import QDialog, QLineEdit, QMessageBox
from ui_login import Ui_Dialog
from api_session import LoginSession
from sidebar import Sidebar  # Assure-toi que le chemin d'importation est correct

class LoginScreen(QDialog, Ui_Dialog):
    def __init__(self, widget):
        super().__init__()
        self.setupUi(self)
        self.widget = widget
        self.setWindowTitle('Ventalis - Login')
        self.pwd_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.connexion_btn.clicked.connect(self.check_login)

    def check_login(self):
        email = self.email_input.text()
        password = self.pwd_input.text()
        try:
            # Utiliser get_instance pour initialiser ou récupérer l'instance singleton.
            login_session = LoginSession.get_instance(email, password)
            QMessageBox.information(self, 'Login Successful', f'Bonjour {email}.')
            # Transition vers Sidebar avec l'instance de session.
            self.transition_to_sidebar(login_session)
        except Exception as e:
            QMessageBox.warning(self, 'Login Failed', str(e))

    def transition_to_sidebar(self, login_session):
        sidebar = Sidebar(login_session)
        self.widget.addWidget(sidebar)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)



