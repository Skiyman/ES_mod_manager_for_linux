import json
import os
import time

import requests
from bs4 import BeautifulSoup

from src.backend.consts import HEADERS


class Parser:
    def __init__(self, enabled, disabled):
        self.steam_url = "https://steamcommunity.com/sharedfiles/filedetails/?id="

        self.enabled_mods_folder = enabled
        self.disabled_mods_folder = disabled

    def get_mods_data(self):
        mods_data = {}
        mods_ids = os.listdir(self.enabled_mods_folder) + os.listdir(self.disabled_mods_folder)

        for mod_id in mods_ids:
            time.sleep(0.1)

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
            mod_name = mod_name.text.replace("\n", "").strip()

            mods_data[mod_id] = {
                "name": mod_name,
                "status": "enabled"
            }

        return mods_data

    def fill_mods_db(self):
        mods_data = self.get_mods_data()

        if mods_data:
            with open("src/settings/mods_db.json", 'w') as file:
                json.dump(mods_data, file, indent=4, ensure_ascii=False)
                file.truncate()

            return mods_data

    def get_mods_db(self):
        try:
            with open('src/settings/mods_db.json', 'r') as file:
                mods_db = json.load(file)
                if len(mods_db) == 0:
                    mods_db = self.fill_mods_db()

            return mods_db
        except FileNotFoundError:
            return self.fill_mods_db()

if __name__ == "__main__":
    enabled_mods_folder = '/home/skiyman/.steam/debian-installation/steamapps/workshop/content/331470/'
    disabled_mods_folder = "../../disabled"
    parser = Parser(enabled=enabled_mods_folder, disabled=disabled_mods_folder)
    parser.fill_mods_db()
