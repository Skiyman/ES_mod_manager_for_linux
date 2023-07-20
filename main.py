import sys

from PyQt5.QtWidgets import QApplication

from src.UI.MainWindow import MainWindow
from src.backend.mods_editor import ModsEditor

if __name__ == "__main__":

    app = QApplication(sys.argv)
    settings = ModsEditor.get_settings()
    m = MainWindow(settings)
    m.show()
    sys.exit(app.exec_())
