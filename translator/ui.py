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

class TranslatorApp(ctk.CTK):
    def __int__(self):
        super().__init__()

        self.title("Translator")
        self.geometry("560x520")
        self.minsize(480, 480)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self._bulid_wigets()
        self._ensure_history_file()


    def _bulid_wigets(self):
        ...

    def _ensure_history_file(self):
        if not os.path.exists(HISTORY_FILE):
            with open(HISTORY_FILE, "w") as f:
                json.dump([], f, indent=2)

    def _save_history(self, original_text, result, source_code, target_code, engine):
        try:
            with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                history = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            history = []

        history.append({
            "timestamp": datetime.now().isoformat(timespec="seconds"),
            "engine": engine,
            "source": source_code,
            "target": target_code,
            "input": original_text,
            "output": result
        })

        with open(HISTORY_FILE, "w") as f:
            json.dump(history, f, indent=2)


    def _run_translation(self, text, source_code, target_code, engine):
        try:
            result = translate_text(
                text,
                source=source_code,
                target=target_code,
                engine=engine
            )
            self.after(
                0,
                self._on_translation_success,
                text,
                result,
                source_code,
                target_code,
                engine
            )
        except TranslationError as e:
            self.after(0, self._on_translation_error, str(e))