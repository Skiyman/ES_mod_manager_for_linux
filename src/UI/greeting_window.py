import json
import os
from pathlib import Path

from PyQt5.QtWidgets import QDialog, QFileDialog

from UI.qtClass.greeting_window_qt import Ui_Dialog
from backend.consts import STEAM_PATH, DISABLED_PATH_TEMPLATE, CONFIG_TEMPLATE


class GreetingWindow(Ui_Dialog, QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.enable_folder = ""
        self.disable_folder = ""

        self.home_directory = os.path.expanduser('~')

        self.browse_enable_folder_button.clicked.connect(lambda: self.select_path(True))
        self.browse_disable_folder_button.clicked.connect(lambda: self.select_path(False))

        self.apply_button.clicked.connect(self.create_config)

        self.create_path()

    def create_path(self):
        steam_directory = self.home_directory + STEAM_PATH
        disabled_folder_path = self.home_directory + DISABLED_PATH_TEMPLATE

        if os.path.exists(steam_directory):
            self.enable_folder_name.setText(steam_directory)
            self.enable_folder = steam_directory
        else:
            self.enable_folder_name.setText(self.home_directory)
            self.enable_folder = self.home_directory

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
        config["first_launch"] = False

        working_directory = os.getcwd()
        disabled_folder_path = self.home_directory + DISABLED_PATH_TEMPLATE

        if disabled_folder_path == self.disable_folder:
            Path(disabled_folder_path).mkdir(parents=True, exist_ok=True)

        Path(self.home_directory + "/.config/esmodmanager").mkdir(parents=True, exist_ok=True)

        with open(self.home_directory + "/.config/esmodmanager/config.json", "w") as file:
            json.dump(config, file, indent=4, ensure_ascii=False)
            file.truncate()

        self.close()
