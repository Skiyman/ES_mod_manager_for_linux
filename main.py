import sys

from PySide6.QtWidgets import QApplication

from src.UI.main_window import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    app.exec()

