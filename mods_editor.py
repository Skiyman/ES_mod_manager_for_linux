import json
import os
import shutil
import sys
import time
import subprocess

import requests
from PyQt5.QtWidgets import QMainWindow, QApplication
from bs4 import BeautifulSoup

from GUI import Ui_Es_mod_namager_linux


class ModsEditor(object):
    def __init__(self):
        self.mods_id = None
        self.mods_db = {}
        self.enabled_mods_folder = "/home/skiyman/programming/pythonProject/ES_mod_manager_linux/mods/"
        self.disabled_mods_folder = "/home/skiyman/programming/pythonProject/ES_mod_manager_linux/disabled/"

    def check_new_mods(self):
        mods_db = self.update_mods_db()
        if len(os.listdir(self.enabled_mods_folder) + os.listdir(self.disabled_mods_folder)) != len(mods_db):
            self.load_mods_db()

    # Создает json-файл в котором хранятся id модов и их названия, полученные через парсинг steam-а
    def load_mods_db(self):
        self.mods_db = self.update_mods_db()
        self.mods_id = os.listdir(self.enabled_mods_folder) + os.listdir(self.disabled_mods_folder)
        HEADERS = {
            "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/101.0.4951.67 Safari/537.36'
        }

        time.sleep(0.1)

        for mod_id in self.mods_id:
            if mod_id not in self.mods_db:
                URL = "https://steamcommunity.com/sharedfiles/filedetails/?id=" + mod_id
                r = requests.sessions.Session()
                r = requests.get(url=URL, headers=HEADERS)

                soup = BeautifulSoup(r.text, "lxml")

                try:
                    name = soup.find("div", class_="workshopItemTitle")
                    name = name.text.replace("\n", "").strip()
                except AttributeError:
                    print("Мода с таким id не существует. Пожалуйста, проверьте на корректность выбранную папку: ",
                          mod_id)
                    name = "ERROR! Мод не был найден в мастерской Steam. Задайте имя самостоятельно"

                self.mods_db[mod_id] = {
                    "mod_name": name,
                    "Work_status": "Enabled"
                }

                with open('mods_db.json', "w") as file:
                    json.dump(self.mods_db, file, indent=4, ensure_ascii=False)
                    file.truncate()

        return self.mods_db

    def update_mods_db(self):
        try:
            with open("mods_db.json", "r") as file:
                self.mods_db = json.load(file)
        except FileNotFoundError:
            self.mods_db = {}

        return self.mods_db

    def delete_mod(self, mod_id):
        with open("mods_db.json", "r+") as file:
            self.mods_db = json.load(file)
            del self.mods_db[mod_id]

            file.seek(0)
            json.dump(self.mods_db, file, indent=4, ensure_ascii=False)
            file.truncate()
        print("Mod was deleted")

    def change_mod_status(self, mod_id, status):
        with open("mods_db.json", "r+") as file:
            self.mods_db = json.load(file)
            self.mods_db[str(mod_id)]["Work_status"] = status

            file.seek(0)
            json.dump(self.mods_db, file, indent=4, ensure_ascii=False)
            file.truncate()

        return self.mods_db

    def mod_replace(self, mod_id):
        self.mods_db = self.update_mods_db()

        if self.mods_db[mod_id]["Work_status"] == "Enabled":
            try:
                shutil.move(self.enabled_mods_folder + mod_id, self.disabled_mods_folder)
                self.mods_db = self.change_mod_status(mod_id, "Disabled")

            except shutil.Error:
                print("Мод уже включен")
            except FileNotFoundError:
                self.delete_mod(mod_id)

        elif self.mods_db[mod_id]["Work_status"] == "Disabled":
            try:
                shutil.move(self.disabled_mods_folder + mod_id, self.enabled_mods_folder)
                self.mods_db = self.change_mod_status(mod_id, "Enabled")

            except shutil.Error:
                print("Мод уже выключен")
            except FileNotFoundError:
                self.delete_mod(mod_id)


class MainWindow(Ui_Es_mod_namager_linux, QMainWindow):
    def __init__(self):

        super().__init__()
        self.setupUi(self)

        self.btn_update_mods_db.clicked.connect(self.fill_mods_lists)
        self.enabled_mods_list.itemDoubleClicked.connect(self.clicked_item_replace)
        self.disabled_mods_list.itemDoubleClicked.connect(self.clicked_item_replace)
        self.btn_Launch_es.clicked.connect(self.run_es)

        self.mod_names_dict = {}
        self.fill_mods_lists()

    def clicked_item_replace(self, item):

        editor = ModsEditor()
        mods_db = editor.update_mods_db()
        if mods_db == {}:
            mods_db = editor.load_mods_db()
        mod_id = self.mod_names_dict[item.text()]
        editor.mod_replace(self.mod_names_dict[item.text()])

        self.fill_mods_lists()

    def fill_mods_lists(self):

        self.enabled_mods_list.clear()
        self.disabled_mods_list.clear()

        editor = ModsEditor()
        mods_db = editor.update_mods_db()
        if mods_db == {}:
            mods_db = editor.load_mods_db()

        self.enabled_mods_list.setSortingEnabled(True)
        self.disabled_mods_list.setSortingEnabled(True)

        for mod in mods_db:
            if mods_db[mod]['Work_status'] == "Enabled":
                self.mod_names_dict[mods_db[mod]["mod_name"]] = mod
                self.enabled_mods_list.addItem(mods_db[mod]['mod_name'])
            else:
                self.mod_names_dict[mods_db[mod]["mod_name"]] = mod
                self.disabled_mods_list.addItem(mods_db[mod]['mod_name'])

        print("update successful")

    def run_es(self):
        subprocess.call('steam steam://rungameid/331470', shell=True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    m = MainWindow()
    m.show()
    sys.exit(app.exec_())
    # editor = mods_editor()
    # editor.check_new_mods()
