import json
from pathlib import Path

from PySide6 import QtWidgets
from PySide6.QtWidgets import QFileDialog

from src.UI.qtClass.settingsWindow_qt import Ui_SettingsWindow


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
            print("Ошибка! Файл конфигурации не был найден. Переустановите приложение.")
            return {}

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
        if self.config["move_mods_before_launch_game"]:
            self.before_game_start_rb.setChecked(True)
        elif not self.config["move_mods_before_launch_game"]:
            self.on_switch_rb.setChecked(True)

        if self.config["update_on_launch"]:
            self.on_launch_update_rb.setChecked(True)
        elif not self.config["update_on_launch"]:
            self.on_button_click_rb.setChecked(True)

        self.enabel_folder_name.setText(self.config["enabled_mods_folder"])
        self.disabel_folder_name.setText(self.config["disabled_mods_folder"])

    def change_settings(self, setting: str, option):
        with open("src/settings/config.json", 'w') as file:
            self.config[setting] = option
            json.dump(self.config, file, indent=4, ensure_ascii=False)
            file.truncate()

        self.main_window.update_config(config=self.config)

        return self.config

    def change_mod_move_method(self):
        if self.before_game_start_rb.isChecked():
            self.change_settings(setting="move_mods_before_launch_game", option=True)
        elif self.on_switch_rb.isChecked():
            self.change_settings(setting="move_mods_before_launch_game", option=False)

    def change_update_method(self):
        if self.on_button_click_rb.isChecked():
            self.change_settings(setting="update_on_launch", option=False)
        elif self.on_launch_update_rb.isChecked():
            self.change_settings(setting="update_on_launch", option=True)
