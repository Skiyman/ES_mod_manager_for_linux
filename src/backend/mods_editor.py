import json
import os.path
import shutil
import subprocess
import time
from threading import Thread

import psutil

from src.backend.parser import Parser


class ModsEditor(object):
    def __init__(self):
        self.parser = None
        self.enabled_mods_folder = ""
        self.disabled_mods_folder = ""

        self.mods_db = {}
        self.settings = {}
        self.config_editor()

    @staticmethod
    def get_settings():
        with open('src/settings/config.json', 'r') as file:
            settings = json.load(file)

        return settings

    @staticmethod
    def get_process_pid(pid_name: str):
        pid = None

        for process in psutil.process_iter(['pid', 'name']):
            if pid_name in process.name():
                pid = process.pid

        return pid

    def config_editor(self):
        self.settings = self.get_settings()

        self.enabled_mods_folder = self.settings['enabled_mods_folder']
        self.disabled_mods_folder = self.settings['disabled_mods_folder']

        self.parser = Parser(enabled=self.enabled_mods_folder, disabled=self.disabled_mods_folder)
        self.mods_db = self.parser.get_mods_db()

    def mod_switcher(self, mod_id):
        if self.settings["mod_move_method"] == 'before_game_launch':
            self.mods_db = self.parser.change_mod_status(mod_id)
        elif self.settings["mod_move_method"] == 'on_switch':
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
            print("Мод уже перемещен")
        except FileNotFoundError:
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

        while es_pid is None and operation_count < 10:
            es_pid = self.get_process_pid(self.settings['es_process_name'])
            operation_count += 1
            time.sleep(2)

        if es_pid is not None:
            print('Начинаю смотреть')
            while psutil.pid_exists(es_pid):
                time.sleep(1)
        print("Возвращаю обратно")
        self.replace_all_mods(mode='on')

    def run_es(self):
        if self.settings['mod_move_method'] == 'before_game_launch':
            self.replace_all_mods()

        subprocess.run('steam steam://rungameid/331470 %U', shell=True, check=True)

        if self.settings['mod_move_method'] == 'before_game_launch':
            es_checker = Thread(target=self.check_es_process)
            es_checker.start()
