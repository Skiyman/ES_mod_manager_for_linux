import json

from src.backend.consts import config_template

from pathlib import Path

from PySide6.QtWidgets import QFileDialog

from src.UI.settingsWindow_qt import Ui_SettingsWindow
from PySide6 import QtCore, QtGui, QtWidgets


class SettingsWindow(Ui_SettingsWindow, QtWidgets.QWidget):
    def __init__(self, window):
        super().__init__()
        self.setupUi(self)

        self.main_window = window
        self.config = self.get_settings()
        self.setup_fields()

        self.before_game_start_rb.clicked.connect(self.change_mod_move_method)
        self.on_switch_rb.clicked.connect(self.change_mod_move_method)

        self.on_button_click_rb.clicked.connect(self.change_update_method)
        self.on_launch_update_rb.clicked.connect(self.change_update_method)

        self.browse_enabel_folder_button.clicked.connect(lambda: self.select_folder("enable_folder"))
        self.browse_disable_folder_button.clicked.connect(lambda: self.select_folder("disable_folder"))

    @staticmethod
    def get_settings():
        try:
            with open("src/settings/config.json", 'r') as file:
                config = json.load(file)

            return config
        except FileNotFoundError:
            with open("src/settings/config.json", "w") as file:
                json.dump(config_template, file, indent=4, ensure_ascii=False)
                file.truncate()

    def select_folder(self, folder):
        dir_name = QFileDialog.getExistingDirectory(self, "Выберите папку")
        if dir_name:
            path = Path(dir_name)

            if folder == "enable_folder":
                self.change_settings(setting="enabled_mods_folder", option=str(path))
                self.enabel_folder_name.setText(str(path))
            if folder == "disable_folder":
                self.change_settings(setting="disabled_mods_folder", option=str(path))
                self.disabel_folder_name.setText(str(path))

    def setup_fields(self):
        if self.config["mod_move_method"] == "before_game_launch":
            self.before_game_start_rb.setChecked(True)
        elif self.config["mod_move_method"] == "on_switch":
            self.on_switch_rb.setChecked(True)

        if self.config["when_update"] == "on_launch":
            self.on_launch_update_rb.setChecked(True)
        elif self.config["when_update"] == "on_click":
            self.on_button_click_rb.setChecked(True)

        self.enabel_folder_name.setText(self.config["enabled_mods_folder"])
        self.disabel_folder_name.setText(self.config["disabled_mods_folder"])

    def change_settings(self, setting: str, option: str):
        with open("src/settings/config.json", 'w') as file:
            self.config[setting] = option
            json.dump(self.config, file, indent=4, ensure_ascii=False)
            file.truncate()

        self.main_window.update_config(config=self.config)

        return self.config

    def change_mod_move_method(self):
        if self.before_game_start_rb.isChecked():
            self.change_settings(setting="mod_move_method", option="before_game_launch")
        elif self.on_switch_rb.isChecked():
            self.change_settings(setting="mod_move_method", option="on_switch")

    def change_update_method(self):
        if self.on_button_click_rb.isChecked():
            self.change_settings(setting="when_update", option="on_click")
        elif self.on_launch_update_rb.isChecked():
            self.change_settings(setting="when_update", option="on_launch")
