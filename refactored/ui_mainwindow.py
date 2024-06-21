from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout
from sidebar import Sidebar
from maincontent import MainContent

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Mon Application')
        self.resize(1376, 857)  # Taille initiale basée sur ton code

        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)

        self.layout = QHBoxLayout(self.centralWidget)
        self.sidebar = Sidebar(self)
        self.mainContent = MainContent(self)

        self.layout.addWidget(self.sidebar)
        self.layout.addWidget(self.mainContent)

        self.initUIConnections()

    def initUIConnections(self):
        self.sidebar.menu_btn.toggled.connect(self.handleToggleSidebar)

    def handleToggleSidebar(self, checked):
        # Mise à jour pour suivre le toggle du sidebar
        if checked:
            self.sidebar.setFixedWidth(50)
        else:
            self.sidebar.setFixedWidth(200)
        self.mainContent.updateUI(checked)  # Méthode pour ajuster l'interface du contenu principal
