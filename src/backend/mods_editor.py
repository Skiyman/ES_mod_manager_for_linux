import json
import shutil
import subprocess
import time
import asyncio
from threading import Thread

import psutil

from src.backend.parser import Parser


class ModsEditor(object):
    def __init__(self):
        self.parser = None
        self.enabled_mods_folder = None
        self.disabled_mods_folder = None

        self.mods_db = {}
        self.settings = {}
        self.config_editor()

    def config_editor(self):
        self.settings = self.get_settings()
        self.enabled_mods_folder = self.settings['enabled_mods_folder']
        self.disabled_mods_folder = self.settings['disabled_mods_folder']

        self.parser = Parser(enabled=self.enabled_mods_folder, disabled=self.disabled_mods_folder)
        self.mods_db = self.parser.get_mods_db()

    @staticmethod
    def get_settings():
        with open('src/settings/settings.json', 'r') as file:
            settings = json.load(file)

        return settings

    def delete_mod(self, mod_id):
        with open("src/settings/mods_db.json", "r+") as file:
            self.mods_db = json.load(file)
            del self.mods_db[mod_id]

            file.seek(0)
            json.dump(self.mods_db, file, indent=4, ensure_ascii=False)
            file.truncate()

    def change_mod_status(self, mod_id):
        with open("src/settings/mods_db.json", "r+") as file:
            self.mods_db = json.load(file)
            if self.mods_db[str(mod_id)]["status"] == "enabled":
                self.mods_db[str(mod_id)]["status"] = "disabled"
            else:
                self.mods_db[str(mod_id)]["status"] = "enabled"
            file.seek(0)
            json.dump(self.mods_db, file, indent=4, ensure_ascii=False)
            file.truncate()

        return self.mods_db

    def mod_replace(self, mod_id):
        if self.mods_db[mod_id]["status"] == "enabled":
            try:
                shutil.move(self.enabled_mods_folder + mod_id, self.disabled_mods_folder)
                self.mods_db = self.change_mod_status(mod_id)
            # except shutil.Error:
            #     pass  # Нужно будет добавить описание ошибки
            except FileNotFoundError:
                self.delete_mod(mod_id)

        elif self.mods_db[mod_id]["status"] == "disabled":
            try:
                shutil.move(self.disabled_mods_folder + mod_id, self.enabled_mods_folder)
                self.mods_db = self.change_mod_status(mod_id)

            except shutil.Error:
                pass  # То же самое
            except FileNotFoundError:
                self.delete_mod(mod_id)

    @staticmethod
    def get_es_pid():
        es_pid = None
        # Лучше проверять наличие сразу тут, чтобы не ебаться ниже
        for process in psutil.process_iter(['pid', 'name']):
            if 'Everlasting Sum' in process.name():
                es_pid = process.pid

        return es_pid

    def check_es_process(self):
        time.sleep(10)
        print("start")

        es_pid = self.get_es_pid()

        if es_pid is not None:
            # Сюда надо добавить функцию для перемещения модов
            while psutil.pid_exists(es_pid):
                # Цикл будет жить, пока существует процесс бл. Т.к. он работает в отдельном потоке,
                # то и приложение ложиться не будет
                try:
                    if psutil.pid_exists(es_pid):
                        print('Still working')
                except TypeError:
                    print(es_pid)
                    continue
                time.sleep(1)

    def run_es(self):
        subprocess.run('steam steam://rungameid/331470 %U', shell=True, check=True)

        es_checker = Thread(target=self.check_es_process)
        es_checker.start()


if __name__ == "__main__":
    editor = ModsEditor()
