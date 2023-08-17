import json
import os

from PyQt5.QtCore import QTranslator

from backend.consts import ENGLISH_TRANSLATES


class Translator:
    def __init__(self, main_window, settings_window, app):
        super().__init__()
        self._translators = []
        self.app = app
        self.main_window = main_window
        self.settings_window = settings_window

    @staticmethod
    def change_config_lang(lang):
        home_directory = os.path.expanduser('~')
        config_path = home_directory + "/.config/esmodmanager/config.json"

        with open(config_path, "r+") as file:
            settings = json.load(file)
            settings["language"] = lang

            file.seek(0)
            json.dump(settings, file)
            file.truncate()

    def set_language(self, lang):
        def set_translators():
            for translator in self._translators:
                self.app.installTranslator(translator)

        def del_translators():
            for translator in self._translators:
                self.app.removeTranslator(translator)

        del_translators()
        self._translators.clear()

        if lang == "en":
            translation_files = os.listdir(ENGLISH_TRANSLATES)
            for file in translation_files:
                self._translators.append(QTranslator())
                self._translators[-1].load(ENGLISH_TRANSLATES + file)

            set_translators()
        else:
            del_translators()
            self._translators.clear()

        self.main_window.retranslateUi(self.main_window)
        self.settings_window.retranslateUi(self.settings_window)

        self.main_window.config['language'] = lang
        self.settings_window.config['language'] = lang
        self.change_config_lang(lang)
