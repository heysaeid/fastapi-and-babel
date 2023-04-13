import os
import gettext
from fastapi import FastAPI


class Translator:
    def __init__(self, locale: str, domain: str, app: FastAPI) -> None:
        self.locale = locale
        self.domain = domain
        self.translation = None

    def load_translation(self):
        localedir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'locales')
        localedir = os.path.normpath(localedir)
        translation = gettext.translation(self.domain, localedir, languages=[self.locale])
        self.translation = translation

    def get_translation(self):
        if not self.translation:
            self.load_translation()
        return self.translation

    def gettext(self, message):
        translation = self.get_translation()
        return translation.gettext(message)

    def ngettext(self, singular, plural, n):
        translation = self.get_translation()
        return translation.ngettext(singular, plural, n)