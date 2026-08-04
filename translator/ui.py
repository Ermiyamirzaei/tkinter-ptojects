import threading
import json
import os
from datetime import datetime
import customtkinter as ctk
from api import translate_text, TranslationError

HISTORY_FILE = os.path.join(os.path.dirname(__file__), "history.json")

LANGUAGES = {
    "Auto Detect": "auto",
    "Persian": "fa",
    "English": "en",
    "Arabic": "ar",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Turkish": "tr",
    "Russian": "ru",
    "Chinese": "zh",
    "Korean": "ko",
    "Japanese": "ja",
}
LANG_NAMES = list(LANGUAGES.keys())

ENGINES = ["yandex", "google", "microsoft"]
