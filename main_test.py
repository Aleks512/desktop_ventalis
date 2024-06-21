from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
import sys

app = QApplication(sys.argv)
loader = QUiLoader()

window = loader.load('sidebar3.ui', None)
if not window:
    print("Erreur lors du chargement du fichier .ui")
    sys.exit(-1)

window.show()
sys.exit(app.exec())
