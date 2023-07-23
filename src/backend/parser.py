import json
import os
import time

import requests
from bs4 import BeautifulSoup

from src.backend.consts import HEADERS


class Parser:
    def __init__(self, enabled, disabled):
        self.steam_url = "https://steamcommunity.com/sharedfiles/filedetails/?id="

        self.mods_db = {}
        self.enabled_mods_folder = enabled
        self.disabled_mods_folder = disabled

        self.mods_db = self.get_mods_db()

    def get_mods_id_list(self):
        return os.listdir(self.enabled_mods_folder) + os.listdir(self.disabled_mods_folder)

    def parse_mod_name(self, mod_id):
        _cookies = {
            f'wants_mature_content_item_{mod_id}': "1",
            'Steam_Language': 'russian',
        }

        _url = self.steam_url + mod_id

        try:
            _request = requests.get(headers=HEADERS, url=_url, cookies=_cookies).text

        except requests.exceptions.ConnectionError:
            # В будущем надо будет сделать окно, которое будет это выводить или просто где-то писать
            # (Лучше просто возвращать значение False и уже как мне надо его обрабатывать)
            return False

        mod_page = BeautifulSoup(_request, "lxml")
        mod_name = mod_page.find("div", class_="workshopItemTitle")
        if mod_name is not None:
            mod_name = mod_name.text.replace("\n", "").strip()

            return mod_name

        return "Ошибка! Мод не был найден в мастерской Steam. Задайте имя самостоятельно"

    def create_mod_data(self, mod_id):
        mod_name = self.parse_mod_name(mod_id)
        if not mod_name:
            raise ConnectionError("Отсутствует подключение к интернету")

        mod_data = {
            "name": mod_name,
            "status": "enabled"
        }

        return mod_data

    def get_mods_data(self):
        mod_folders = self.get_mods_id_list()

        for mod_id in mod_folders:
            if mod_id not in self.mods_db:
                time.sleep(0.1)
                self.mods_db[mod_id] = self.create_mod_data(mod_id)

        return self.mods_db

    def find_removed_mods(self):
        mod_folders = self.get_mods_id_list()

        for mod_id in self.mods_db:
            if mod_id not in mod_folders:
                self.delete_mod(mod_id)

    def fill_mods_db(self):
        self.find_removed_mods()
        self.mods_db = self.get_mods_data()

        if self.mods_db:
            with open("src/settings/mods_db.json", 'w') as file:
                json.dump(self.mods_db, file, indent=4, ensure_ascii=False)
                file.truncate()

            return self.mods_db

        return {}

    def get_mods_db(self):
        try:
            with open('src/settings/mods_db.json', 'r') as file:
                self.mods_db = json.load(file)
                if len(self.mods_db) == 0 and len(self.get_mods_id_list()) != 0:
                    self.mods_db = self.fill_mods_db()

            return self.mods_db
        except FileNotFoundError:
            return self.fill_mods_db()

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

            elif self.mods_db[str(mod_id)]["status"] == "disabled":
                self.mods_db[str(mod_id)]["status"] = "enabled"
            file.seek(0)
            json.dump(self.mods_db, file, indent=4, ensure_ascii=False)
            file.truncate()

        return self.mods_db


if __name__ == "__main__":
    enabled_mods_folder = '/home/skiyman/.steam/debian-installation/steamapps/workshop/content/331470/'
    disabled_mods_folder = "../../disabled"
    parser = Parser(enabled=enabled_mods_folder, disabled=disabled_mods_folder)
