import json
import os
from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QFileDialog

from src.UI.qtClass.greeting_window_qt import Ui_Dialog
from src.backend.consts import STEAM_PATH, DISABLED_PATH_TEMPLATE, CONFIG_TEMPLATE


class GreetingWindow(Ui_Dialog, QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.enable_folder = ""
        self.disable_folder = ""

        self.browse_enable_folder_button.clicked.connect(lambda: self.select_path(True))
        self.browse_disable_folder_button.clicked.connect(lambda: self.select_path(False))

        self.apply_button.clicked.connect(self.create_config)

        self.create_path()

    def create_path(self):
        home_directory = os.path.expanduser('~')
        steam_directory = home_directory + STEAM_PATH

        working_directory = os.getcwd()
        disabled_folder_path = working_directory + DISABLED_PATH_TEMPLATE
        if os.path.exists(home_directory):
            self.enable_folder_name.setText(steam_directory)
            self.enable_folder = steam_directory
        else:
            self.enable_folder_name.setText(home_directory)
            self.enable_folder = home_directory

        self.disable_folder_name.setText(disabled_folder_path)
        self.disable_folder = disabled_folder_path

    def select_path(self, enable_folder):
        dir_name = QFileDialog.getExistingDirectory(self, "Выберите папку")
        if dir_name:
            path = Path(dir_name)

            if enable_folder:
                self.enable_folder_name.setText(str(path))
                self.enable_folder = str(path)
            if not enable_folder:
                self.disable_folder_name.setText(str(path))
                self.disable_folder = str(path)

    def create_config(self):
        config = CONFIG_TEMPLATE
        config["enabled_mods_folder"] = self.enable_folder
        config["disabled_mods_folder"] = self.disable_folder

        with open("src/settings/config.json", "w") as file:
            json.dump(config, file, indent=4, ensure_ascii=False)
            file.truncate()

        self.close()