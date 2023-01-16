import os
import requests
import time
import json
import shutil

from bs4 import BeautifulSoup


class mods_editor(object):
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
        self.mods_id = os.listdir(self.enabled_mods_folder) + os.listdir(self.disabled_mods_folder)
        HEADERS = {
            "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'}

        time.sleep(0.1)

        for mod_id in self.mods_id:
            URL = "https://steamcommunity.com/sharedfiles/filedetails/?id=" + mod_id
            r = requests.sessions.Session()
            r = requests.get(url=URL, headers=HEADERS)

            soup = BeautifulSoup(r.text, "lxml")

            try:
                name = soup.find("div", class_="workshopItemTitle")
                name = name.text.replace("\n", "").strip()
            except AttributeError:
                print("Мода с таким id не существует. Пожалуйста, проверьте на корректность выбранную папку: ", mod_id)
                name = "ERROR! Мод не был найден в мастерской Steam. Задайте имя самостоятельно"

            self.mods_db[mod_id] = {
                "mod_name": name,
                "Work_status": "Enabled"
            }

        with open("/home/skiyman/programming/pythonProject/ES_mod_manager_linux/mods_db.json", "w") as file:
            json.dump(self.mods_db, file, indent=4, ensure_ascii=False)
            file.truncate()

    def update_mods_db(self):
        with open("/home/skiyman/programming/pythonProject/ES_mod_manager_linux/mods_db.json", "r") as file:
            self.mods_db = json.load(file)

        return self.mods_db

    def mod_replace(self, mod_id):
        self.mods_db = self.update_mods_db()

        if self.mods_db[mod_id]["Work_status"] == "Enabled":
            try:
                shutil.move(self.enabled_mods_folder + mod_id, self.disabled_mods_folder)

                with open("/home/skiyman/programming/pythonProject/ES_mod_manager_linux/mods_db.json", "r+") as file:
                    obj = json.load(file)
                    obj[str(mod_id)]["Work_status"] = "Disabled"

                    file.seek(0)
                    json.dump(obj, file, indent=4, ensure_ascii=False)
                    file.truncate()

                self.mods_db = self.update_mods_db()

            except shutil.Error:
                print("Мод уже включен")

        elif self.mods_db[mod_id]["Work_status"] == "Disabled":
            try:
                shutil.move(self.disabled_mods_folder + mod_id, self.enabled_mods_folder)

                with open("/home/skiyman/programming/pythonProject/ES_mod_manager_linux/mods_db.json", "r+") as file:
                    obj = json.load(file)
                    obj[str(mod_id)]["Work_status"] = "Enabled"

                    file.seek(0)
                    json.dump(obj, file, indent=4, ensure_ascii=False)
                    file.truncate()

                self.mods_db = self.update_mods_db()
            except shutil.Error:
                print("Мод уже выключен")


if __name__ == "__main__":
    editor = mods_editor()
    editor.check_new_mods()
