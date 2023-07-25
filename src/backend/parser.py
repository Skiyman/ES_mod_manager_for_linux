import json
import os
import time
import asyncio
import aiohttp

import requests
from bs4 import BeautifulSoup

from src.backend.consts import HEADERS


class Parser:
    def __init__(self, enabled, disabled):
        self.parse_thread = None
        self.steam_url = "https://steamcommunity.com/sharedfiles/filedetails/?id="

        self.mods_db = {}
        self.enabled_mods_folder = enabled
        self.disabled_mods_folder = disabled

        self.mods_db = self.get_mods_db()

    def get_mods_id_list(self):
        return os.listdir(self.enabled_mods_folder) + os.listdir(self.disabled_mods_folder)

    async def parse_mod_name(self, mod_id, session):
        _cookies = {
            f'wants_mature_content_item_{mod_id}': "1",
            'Steam_Language': 'russian',
        }

        _url = self.steam_url + mod_id

        try:
            request = await session.get(headers=HEADERS, url=_url, cookies=_cookies)

        except requests.exceptions.ConnectionError:
            # В будущем надо будет сделать окно, которое будет это выводить или просто где-то писать
            # (Лучше просто возвращать значение False и уже как мне надо его обрабатывать)
            return False

        mod_page = BeautifulSoup(await request.text(), "lxml")
        mod_name = mod_page.find("div", class_="workshopItemTitle")

        if mod_name is not None:
            mod_name = mod_name.text.replace("\n", "").strip()

            return mod_name

        return "Ошибка! Мод не был найден в мастерской Steam. Задайте имя самостоятельно"

    async def create_mod_data(self, mod_id, session):
        mod_name = await self.parse_mod_name(mod_id, session=session)
        if not mod_name:
            raise ConnectionError("Отсутствует подключение к интернету")

        mod_data = {
            "name": mod_name,
            "status": "enabled"
        }
        self.mods_db[mod_id] = mod_data
        print(f"[INFO]Получен мод: {mod_name}")

        return mod_data

    async def get_mods_data(self):
        mod_folders = self.get_mods_id_list()
        tasks = []
        session = aiohttp.ClientSession()

        for mod_id in mod_folders:
            if mod_id not in self.mods_db:
                time.sleep(0.1)
                task = asyncio.create_task(self.create_mod_data(mod_id, session=session))
                tasks.append(task)

        await asyncio.gather(*tasks)
        await session.close()

        self.fill_mods_db()

        return self.mods_db

    def start_parse(self):
        asyncio.run(self.get_mods_data())

    def find_removed_mods(self):
        mod_folders = self.get_mods_id_list()

        for mod_id in self.mods_db:
            if mod_id not in mod_folders:
                self.delete_mod(mod_id)

    def fill_mods_db(self):
        self.find_removed_mods()

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

            return self.mods_db
        except FileNotFoundError:
            with open('src/settings/mods_db.json', 'w') as file:
                json.dump(self.mods_db, file, indent=4, ensure_ascii=False)
                file.truncate()

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
            if mod_id in self.mods_db:
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
    parser.start_parse()
