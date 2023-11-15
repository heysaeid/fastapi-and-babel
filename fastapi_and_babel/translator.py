import os
import gettext as main_gettext
from typing import Optional
from dataclasses import dataclass
from fastapi import FastAPI
from fastapi_and_babel.middleware import Middleware 
from fastapi_and_babel.exceptions import TranslationDirectoryNotFoundException


@dataclass
class BabelConfiguration:
    default_locale: str
    instance: 'FastAPIAndBabel' = None 


class FastAPIAndBabel:
    instance: Optional["FastAPIAndBabel"] = None

    def __init__(
        self, 
        root_dir: str,
        app: FastAPI = None, 
        default_locale: str = "en",
        domain: str = "messages", 
        translation_dir: str = "translations",
        add_default_middleware: bool = False,
    ) -> None:
        FastAPIAndBabel.instance = self
        self.root_dir = root_dir
        self.locale = default_locale
        self.domain = domain
        self.translation_dir = translation_dir
        self.translations = {}
        self.app = app
        
        if self.app:
            app.state.babel = BabelConfiguration(default_locale = self.locale, instance = self)
        
        if add_default_middleware:
            app.add_middleware(Middleware)
        
    def get_root_dir(self) -> str | None:
        current_dir = self.root_dir
        previous_dir = None

        while current_dir != previous_dir:
            package_json_path = os.path.join(current_dir, self.translation_dir)

            if os.path.exists(package_json_path):
                return str(current_dir) + f"/{self.translation_dir}"

            previous_dir = current_dir
            current_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
        
        raise TranslationDirectoryNotFoundException(self.translation_dir)

    def load_translation(self, language: str):
        if language not in self.translations:
            localedir = self.get_root_dir()
            translation = main_gettext.translation(self.domain, localedir, languages=[self.get_current_locale()])
            self.translations[language] = translation
        return self.translations[language]

    def get_translation(self):
        language = self.get_current_locale()
        if language not in self.translations:
            self.translations[language] = self.load_translation(language)
        return self.translations[language]
    
    def get_current_locale(self) -> str:
        return self.app.state.babel.default_locale if self.app else self.locale
    
    def set_default_locale(self, default_locale: str):
        if self.app:
            self.app.state.babel.default_locale = default_locale
        else:
            self.locale = default_locale

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