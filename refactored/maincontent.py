from PySide6.QtWidgets import QWidget, QVBoxLayout, QStackedWidget, QLabel

class MainContent(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.stackedWidget = QStackedWidget(self)
        self.layout.addWidget(self.stackedWidget)
        self.initPages()

    def initPages(self):
        # Ajouter des pages spécifiques comme décrit dans ton code
        self.stackedWidget.addWidget(QLabel("Page 1: Messages Reçus"))
        self.stackedWidget.addWidget(QLabel("Page 2: Créer Message"))
        # etc...

    def updateUI(self, sidebarCollapsed):
        # Réajuster l'UI selon l'état du sidebar
        if sidebarCollapsed:
            self.stackedWidget.setFixedWidth(1000)
        else:
            self.stackedWidget.setFixedWidth(850)
