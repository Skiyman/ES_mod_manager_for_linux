from PySide6.QtWidgets import QMainWindow

from src.UI.MainWindow_qt import Ui_Es_mod_namager_linux
from src.UI.settings_window import SettingsWindow
from src.backend.mods_editor import ModsEditor
from src.backend.parser import Parser


class MainWindow(Ui_Es_mod_namager_linux, QMainWindow):
    def __init__(self):

        super().__init__()
        self.setupUi(self)

        self.settings_window = SettingsWindow(self)
        self.config = SettingsWindow.get_settings()

        self.editor = ModsEditor(self.config)
        self.parser = Parser(self.config['enabled_mods_folder'], self.config['disabled_mods_folder'])


        if self.config["when_update"] == "on_launch":
            self.parser.fill_mods_db()

        self.mod_names_dict = {}
        self.fill_mods_lists()

        self.btn_update_mods_db.clicked.connect(self.update_mod_db)
        self.enabled_mods_list.itemDoubleClicked.connect(self.clicked_item_replace)
        self.disabled_mods_list.itemDoubleClicked.connect(self.clicked_item_replace)
        self.btn_Launch_es.clicked.connect(self.editor.run_es)
        self.btn_enable_all.clicked.connect(self.enable_all)
        self.btn_disable_all.clicked.connect(self.disable_all)

        self.settings_menu.triggered.connect(self.open_settings_menu)

    def open_settings_menu(self):
        self.settings_window.show()

    def clicked_item_replace(self, item):
        self.editor.mod_switcher(self.mod_names_dict[item.text()])
        self.fill_mods_lists()

    def enable_all(self):
        mods_db = self.parser.get_mods_db()

        for mod_id in mods_db:
            if mods_db[mod_id]["status"] == "disabled":
                self.editor.mod_switcher(mod_id)

        self.fill_mods_lists()

    def disable_all(self):
        mods_db = self.parser.get_mods_db()

        for mod_id in mods_db:
            if mods_db[mod_id]["status"] == "enabled":
                self.editor.mod_switcher(mod_id)

        self.fill_mods_lists()

    def update_mod_db(self):
        self.parser.fill_mods_db()
        self.fill_mods_lists()

    def fill_mods_lists(self):
        self.enabled_mods_list.clear()
        self.disabled_mods_list.clear()

        mods_db = self.parser.get_mods_db()

        self.enabled_mods_list.setSortingEnabled(True)
        self.disabled_mods_list.setSortingEnabled(True)

        for mod in mods_db:
            if mods_db[mod]['status'] == "enabled":
                self.mod_names_dict[mods_db[mod]["name"]] = mod
                self.enabled_mods_list.addItem(mods_db[mod]['name'])
            else:
                self.mod_names_dict[mods_db[mod]["name"]] = mod
                self.disabled_mods_list.addItem(mods_db[mod]['name'])

    def update_config(self, config: dict):
        self.config = config

        self.editor.config = config
        self.editor.enabled_mods_folder = self.config['enabled_mods_folder']
        self.editor.disabled_mods_folder = self.config['disabled_mods_folder']
        self.editor.update_mod_move_method()

        self.parser.enabled_mods_folder = self.config['enabled_mods_folder']
        self.parser.disabled_mods_folder = self.config['disabled_mods_folder']
