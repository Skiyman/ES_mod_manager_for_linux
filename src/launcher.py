import os.path
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui

from UI.greeting_window import GreetingWindow
from UI.main_window import MainWindow
from UI.settings_window import SettingsWindow


def main():
    home_directory = os.path.expanduser('~')
    config_path = home_directory + "/.config/esmodmanager/config.json"

    config = SettingsWindow.get_settings()

    app = QApplication(sys.argv)
    app.setDesktopFileName("esmodmanager")
    app.setWindowIcon(QtGui.QIcon('assets/logo.png'))

    if not os.path.exists(config_path) or config["first_launch"]:
        greeting_window = GreetingWindow()
        greeting_window.show()
        app.exec()

    main_window = MainWindow()
    main_window.show()
    app.exec()


if __name__ == "__main__":
    main()
