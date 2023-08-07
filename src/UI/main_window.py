from PyQt5.QtWidgets import QMainWindow

from UI.greeting_window import GreetingWindow
from UI.qtClass.MainWindow_qt import Ui_Es_mod_namager_linux
from UI.settings_window import SettingsWindow
from backend.mods_editor import ModsEditor
from backend.parser import Parser
from backend.qt_threads import ProcessCheckerThread, ModsMoverThread, ParseThread


class MainWindow(Ui_Es_mod_namager_linux, QMainWindow):
    def __init__(self):

        super().__init__()
        self.setupUi(self)
        self.process_checker = None
        self.mods_move_thread = None
        self.parse_thread = None

        self.settings_window = SettingsWindow(self)
        self.config = SettingsWindow.get_settings()

        self.greeting_window = GreetingWindow()

        self.parser = Parser(self.config['enabled_mods_folder'], self.config['disabled_mods_folder'])
        self.editor = ModsEditor(self.config)

        if self.config["update_on_launch"]:
            self.update_mod_db()

        self.mod_names_dict = self.parser.get_mods_db()
        self.connect_buttons()
        self.fill_mods_lists()

    def connect_buttons(self):
        self.btn_update_mods_db.clicked.connect(self.update_mod_db)
        self.enabled_mods_list.itemDoubleClicked.connect(self.clicked_item_replace)
        self.disabled_mods_list.itemDoubleClicked.connect(self.clicked_item_replace)
        self.btn_Launch_es.clicked.connect(self.launch_game)
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

        mod_list = []
        for mod_id in mods_db:
            if mods_db[mod_id]["status"] == "disabled":
                mod_list.append(mod_id)

        self.mods_move_thread = ModsMoverThread(mod_list=mod_list, mods_editor=self.editor)
        self.mods_move_thread.finished.connect(self.fill_mods_lists)
        self.mods_move_thread.start()

    def disable_all(self):
        mods_db = self.parser.get_mods_db()

        mod_list = []
        for mod_id in mods_db:
            if mods_db[mod_id]["status"] == "enabled":
                mod_list.append(mod_id)

        self.mods_move_thread = ModsMoverThread(mod_list=mod_list, mods_editor=self.editor)
        self.mods_move_thread.finished.connect(self.fill_mods_lists)
        self.mods_move_thread.start()

    def update_mod_db(self):
        self.btn_update_mods_db.setEnabled(False)
        self.statusbar.showMessage("Начинаю поиск модов. Пожалуйста, подождите...")
        self.parse_thread = ParseThread(parser=self.parser)

        self.parse_thread.finished.connect(self.fill_mods_lists)
        self.parse_thread.finished.connect(lambda: self.statusbar.showMessage(""))
        self.parse_thread.finished.connect(lambda: self.btn_update_mods_db.setEnabled(True))

        self.parse_thread.start()

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

    def launch_game(self):
        if self.config["move_mods_before_launch_game"]:
            self.btn_Launch_es.setEnabled(False)

            self.editor.replace_all_mods(mode="off")
            self.process_checker = ProcessCheckerThread(self)

            self.process_checker.finished.connect(lambda: self.editor.replace_all_mods(mode="on"))
            self.process_checker.finished.connect(lambda: self.btn_Launch_es.setEnabled(True))

            self.process_checker.start()
        elif not self.config["move_mods_before_launch_game"]:
            ProcessCheckerThread.run_es()

    def update_config(self, config: dict):
        self.config = config

        self.editor.config = config
        self.editor.enabled_mods_folder = self.config['enabled_mods_folder']
        self.editor.disabled_mods_folder = self.config['disabled_mods_folder']
        self.editor.update_mod_move_method()

        self.parser.enabled_mods_folder = self.config['enabled_mods_folder']
        self.parser.disabled_mods_folder = self.config['disabled_mods_folder']
