import sys

from PyQt5.QtWidgets import QApplication

from src.UI.MainWindow import MainWindow

if __name__ == "__main__":

    app = QApplication(sys.argv)
    m = MainWindow()
    m.show()
    sys.exit(app.exec_())
