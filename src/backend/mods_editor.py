import os.path
import shutil
import subprocess
import time
from threading import Thread
from src.UI.settings_window import SettingsWindow

import psutil

from src.backend.parser import Parser


class ModsEditor(object):
    def __init__(self, config):
        self.parser = None

        self.mods_db = {}
        self.config = config
        self.enabled_mods_folder = ""
        self.disabled_mods_folder = ""

        self.config_editor()

    @staticmethod
    def get_process_pid(pid_name: str):
        pid = None

        for process in psutil.process_iter(['pid', 'name']):
            if pid_name in process.name():
                pid = process.pid

        return pid

    def update_mod_move_method(self):
        if self.config["mod_move_method"] == "on_switch":
            for mod_id in self.mods_db:
                if self.mods_db[mod_id]["status"] == "disabled":
                    self.replace_folder(mod_id, self.enabled_mods_folder, self.disabled_mods_folder)
                if self.mods_db[mod_id]["status"] == 'enabled':
                    self.replace_folder(mod_id, self.disabled_mods_folder, self.enabled_mods_folder)

        elif self.config["mod_move_method"] == "before_game_launch" and len(os.listdir(self.disabled_mods_folder)) != 0:
            for mod_id in os.listdir(self.disabled_mods_folder):
                self.replace_folder(mod_id, self.disabled_mods_folder, self.enabled_mods_folder)

    def config_editor(self):
        self.enabled_mods_folder = self.config['enabled_mods_folder']
        self.disabled_mods_folder = self.config['disabled_mods_folder']

        self.parser = Parser(enabled=self.enabled_mods_folder, disabled=self.disabled_mods_folder)
        self.mods_db = self.parser.get_mods_db()

    def mod_switcher(self, mod_id: str):
        if self.config["mod_move_method"] == 'before_game_launch':
            self.mods_db = self.parser.change_mod_status(mod_id)
        elif self.config["mod_move_method"] == 'on_switch':
            self.mods_db = self.parser.change_mod_status(mod_id)
            self.mod_replace(mod_id, self.mods_db[mod_id]['status'])

    def mod_replace(self, mod_id, destination="enabled"):
        if destination == "disabled":
            self.replace_folder(mod_id, self.enabled_mods_folder, self.disabled_mods_folder)

        elif destination == "enabled":
            self.replace_folder(mod_id, self.disabled_mods_folder, self.enabled_mods_folder)

    def replace_folder(self, mod_id, current_folder, destination_folder):
        try:
            shutil.move(current_folder + mod_id, destination_folder)
        except shutil.Error:
            pass
        except FileNotFoundError:
            print(current_folder, destination_folder)
            print("Ошибка")
            if not os.path.exists(destination_folder + mod_id):
                self.parser.delete_mod(mod_id)

    def replace_all_mods(self, mode='off'):
        if mode == 'off':
            for mod_id in self.mods_db:
                if self.mods_db[mod_id]['status'] == 'disabled':
                    self.mod_replace(mod_id, destination="disabled")
        elif mode == "on":
            disabled_mods = os.listdir(self.disabled_mods_folder)
            for mod_id in disabled_mods:
                self.mod_replace(mod_id, destination='enabled')

    def check_es_process(self):
        es_pid = None
        operation_count = 0

        while es_pid is None and operation_count < 20:
            es_pid = self.get_process_pid(self.config['es_process_name'])
            operation_count += 1
            time.sleep(2)

        if es_pid is not None:
            while psutil.pid_exists(es_pid):
                time.sleep(1)

        self.replace_all_mods(mode='on')

    def run_es(self):
        self.config = SettingsWindow.get_settings()

        if self.config['mod_move_method'] == 'before_game_launch':
            self.replace_all_mods()

        subprocess.run('steam steam://rungameid/331470 %U', shell=True, check=True)

        if self.config['mod_move_method'] == 'before_game_launch':
            es_checker = Thread(target=self.check_es_process)
            es_checker.start()
