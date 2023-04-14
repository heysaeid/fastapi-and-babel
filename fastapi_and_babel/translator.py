import os
import gettext
from dataclasses import dataclass
from fastapi import FastAPI
from fastapi_and_babel.middleware import Middleware 


@dataclass
class BabelConfiguration:
    default_locale: str
    instance: 'FastAPIAndBabel' = None 


class FastAPIAndBabel:

    def __init__(self, app: FastAPI, locale: str, domain: str = "messages", translation_directory: str = "translations") -> None:
        self.locale = locale
        self.domain = domain
        self.translation_directory = translation_directory
        self.translation = {}
        self.app = app

        app.state.babel = BabelConfiguration(default_locale = self.locale, instance = self)
        app.add_middleware(Middleware)

    def load_translation(self, language: str):
        if language not in self.translations:
            localedir = os.path.join(os.path.dirname(os.path.abspath(__file__)), self.translation_directory)
            localedir = os.path.normpath(localedir)
            translation = gettext.translation(self.domain, localedir, languages=[self.app.state.babel.default_locale])
            self.translations[language] = translation
        return self.translations[language]

    def get_translation(self):
        language = self.app.state.babel.default_locale
        if language not in self.translations:
            self.translations[language] = self.load_translation(language)
        return self.translation[language]

    def gettext(self, message):
        translation = self.get_translation()
        return translation.gettext(message)

    def ngettext(self, singular, plural, n):
        translation = self.get_translation()
        return translation.ngettext(singular, plural, n)