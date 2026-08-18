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
        self.grid_columnconfigure(0, weight = 1)
        title_label = ctk.CTkLabel(
            self , text="Translator", font=ctk.CTkFont(size=22, weight="bold")

        )
        title_label.grid(row=0, column= 0, pady=(15,10))

        lang_frame = ctk.CTkFrame(self, fg_color="transparent")
        lang_frame.grid(row=1,column=0, padx=20,pady=5, sticky = "ew" )
        lang_frame.grid_columnconfigure((0,1,2), weight=1)

        from_box = ctk.CTkFrame(self, fg_color="transparent")
        from_box.grid(roe=0,column=0,sticky="w")
        ctk.CTkLabel(from_box, text="From:").pack(side="left", padx=(0, 5))
        self.source_menu = ctk.CTkOptionMenu(from_box,values=LANG_NAMES, width=100)
        self.source_menu.set("Auto Detect")
        self.source_menu.pack(side = "left")

        self.swap_btn = ctk.CTkButton(
            lang_frame, text="change", width=36, command=self.swap_languages
        )
        self.swap_btn.grid(row = 0, column=1)

        to_box = ctk.CTkFrame(lang_frame, fg_color="transparent")
        to_box.grid(row=0, column=2, sticky= "e")
        ctk.CTkLabel(to_box, text="To").pack(side ="left", padx=(0, 5))
        self.target_menu = ctk.CTkOptionMenu(to_box, values=LANG_NAMES, width=130)
        self.target_menu.set("Persian")
        self.target_menu.pack(side="left")


        engine_frame = ctk.CTkFrame(self, fg_color="transparent")
        engine_frame.grid(row=2, column=0, pady=(5, 5))
        ctk.CTkLabel(engine_frame, text="Engine:").pack(side="left", padx=(0,5))
        self.engine_menu = ctk.CTkOptionMenu(engine_frame, values=ENGINES, width=120)
        self.engine_menu.set("yandex")
        self.engine_menu.pack(side="left")

                # Input text box
        self.input_box = ctk.CTkTextbox(self, height=140, wrap="word", font=ctk.CTkFont(size=14))
        self.input_box.grid(row=3, column=0, padx=20, pady=10, sticky="ew")
        self.input_box.insert("1.0", "Type your text here...")
        self.input_box.bind("<FocusIn>", self._clear_placeholder)

        # Translate button
        self.translate_btn = ctk.CTkButton(
            self, text="Translate", command=self.on_translate_click, height=36
        )
        self.translate_btn.grid(row=4, column=0, pady=5)

        # Output text box
        self.output_box = ctk.CTkTextbox(self, height=140, wrap="word", font=ctk.CTkFont(size=14))
        self.output_box.grid(row=5, column=0, padx=20, pady=10, sticky="ew")
        self.output_box.configure(state="disabled")

        # Status / error message
        self.status_label = ctk.CTkLabel(self, text="", text_color="gray")
        self.status_label.grid(row=6, column=0, pady=(0, 5))

        # Bottom button row
        bottom_frame = ctk.CTkFrame(self, fg_color="transparent")
        bottom_frame.grid(row=7, column=0, pady=10)

        self.copy_btn = ctk.CTkButton(
            bottom_frame, text="📋 Copy", width=100, command=self.copy_result
        )
        self.copy_btn.pack(side="left", padx=5)

        self.clear_btn = ctk.CTkButton(
            bottom_frame, text="🗑️ Clear", width=100, command=self.clear_all
        )
        self.clear_btn.pack(side="left", padx=5)

        self.theme_btn = ctk.CTkButton(
            bottom_frame, text="Theme", width=100, command=self.toggle_theme
        )
        self.theme_btn.pack(side="left", padx=5)
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

    def _clear_placeholder(self, event=None):
        if self.input_box.get("1.0", "end-1c") == "Type your text here...":
            self.input_box.delete("1.0", "end")


    def swap_languages(self):
        src, tgt = self.source_menu.get(), self.target_menu.get()
        if src == "Auto Detect":
            self.status_label.configure(text="Can't swap when source is Auto Detect.", text_color="orange")
            return
        self.source_menu.set(tgt)
        self.target_menu.set(src)
    def on_translat_click(self):
        ...

    def _on_translations_succses(self, original_text, result, source_code, target_code, engine):
        ...

    def _on_translations_error(self):
        ...

    def copy_result(self):
        ...

    def clear_all(self):
        ...

    def toggle_theme(self):
        ...
#other method added        