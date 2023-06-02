import os
import gettext as main_gettext
from typing import Optional
from dataclasses import dataclass
from fastapi import FastAPI
from fastapi_and_babel.middleware import Middleware 


@dataclass
class BabelConfiguration:
    default_locale: str
    instance: 'FastAPIAndBabel' = None 


class FastAPIAndBabel:
    instance: Optional["FastAPIAndBabel"] = None

    def __init__(
        self, 
        app: FastAPI, 
        root_dir: str,
        locale: str, 
        domain: str = "messages", 
        translation_dir: str = "translations",
    ) -> None:
        FastAPIAndBabel.instance = self
        self.root_dir = root_dir
        self.locale = locale
        self.domain = domain
        self.translation_dir = translation_dir
        self.translations = {}
        self.app = app
        
        app.state.babel = BabelConfiguration(default_locale = self.locale, instance = self)
        app.add_middleware(Middleware)

    def load_translation(self, language: str):
        if language not in self.translations:
            localedir = os.path.join(os.path.dirname(os.path.abspath(self.root_dir)), self.translation_dir)
            localedir = os.path.normpath(localedir)
            translation = main_gettext.translation(self.domain, localedir, languages=[self.app.state.babel.default_locale])
            self.translations[language] = translation
        return self.translations[language]

    def get_translation(self):
        language = self.app.state.babel.default_locale
        if language not in self.translations:
            self.translations[language] = self.load_translation(language)
        return self.translations[language]
    
    def set_default_locale(self, default_locale: str):
        self.app.state.babel.default_locale = default_locale

    def gettext(self, message):
        translation = self.get_translation()
        return translation.gettext(message)

    def ngettext(self, singular, plural, n):
        translation = self.get_translation()
        return translation.ngettext(singular, plural, n)
    
    def get_multi_language_text(self, message: dict):
        translations = {}
        for language in self.translations.keys():
            translation = self.translations[language]
            translations[language] = translation.gettext(message)
        return translations
    

def ensure_instance() -> None:
    if not FastAPIAndBabel.instance:
        raise RuntimeError("An instance of FastAPIAndBabel class has not been created.")
    

def gettext(message: str) -> str:
    ensure_instance()
    return FastAPIAndBabel.instance.gettext(message)


def ngettext(singular, plural, n) -> str:
    ensure_instance()
    return FastAPIAndBabel.instance.ngettext(singular, plural, n)