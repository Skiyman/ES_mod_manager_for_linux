import subprocess
import time
import psutil
from PySide6.QtCore import QThread


class ProcessCheckerThread(QThread):
    def __init__(self, main_window, parent=None):
        super().__init__(parent)
        self.main_window = main_window
        self.config = self.main_window.config

    def run(self):
        self.run_es()
        es_pid = None
        operation_count = 0

        while es_pid is None and operation_count < 20:
            es_pid = self.get_process_pid(self.config['es_process_name'])
            operation_count += 1
            time.sleep(2)

        if es_pid is not None:
            while psutil.pid_exists(es_pid):
                time.sleep(1)

            self.main_window.editor.replace_all_mods(mode='on')

    @staticmethod
    def run_es():
        subprocess.run('steam steam://rungameid/331470 %U', shell=True, check=True)

    @staticmethod
    def get_process_pid(pid_name: str):
        pid = None

        for process in psutil.process_iter(['pid', 'name']):
            if pid_name in process.name():
                pid = process.pid

        return pid


class ModsMoverThread(QThread):
    def __init__(self, mods_editor, mod_list, parent=None):
        super().__init__(parent)
        self.mod_list = mod_list
        self.mods_editor = mods_editor

    def run(self):
        for mod in self.mod_list:
            self.mods_editor.mod_switcher(mod)


class ParseThread(QThread):
    def __init__(self, parser, parent=None):
        super().__init__(parent)
        self.parser = parser

    def run(self):
        self.parser.start_parse()


