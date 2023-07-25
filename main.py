import os.path
import sys

from PySide6.QtWidgets import QApplication

from src.UI.greeting_window import GreetingWindow
from src.UI.main_window import MainWindow
from src.UI.settings_window import SettingsWindow

if __name__ == "__main__":
    config = SettingsWindow.get_settings()

    app = QApplication(sys.argv)

    if not os.path.exists("src/settings/config.json") or config["first_launch"]:
        greeting_window = GreetingWindow()
        greeting_window.show()
        app.exec()

    main_window = MainWindow()
    main_window.show()
    app.exec()
