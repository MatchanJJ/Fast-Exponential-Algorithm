from PyQt5.QtGui import QFontDatabase, QFont
import os

# say thank you to chat gpt for saving ya boi 1 day of stress, thank you chat gpt i love you so much what is life without you i cannot live without you chatgpt chatgpt will you will youuu~~~~~~ fuck you
class FontManager:
    _fonts = {}

    @staticmethod
    def _load_font(path: str):
        abs_path = os.path.abspath(path)
        font_id = QFontDatabase.addApplicationFont(abs_path)
        if font_id == -1:
            print(f"❌ Failed to load font: {path}")
            return None
        
        family = QFontDatabase.applicationFontFamilies(font_id)[0]
        FontManager._fonts[path] = family
        return family

    @classmethod
    def get_font(cls, path: str, size: int = 12) -> QFont:
        if path not in cls._fonts:
            family = cls._load_font(path)
            if not family:
                return QFont()  # fallback to system font
        else:
            family = cls._fonts[path]

        return QFont(family, size)

    # === Specific shortcuts === #
    @classmethod
    def get_ibm_plex(cls, size=12):
        return cls.get_font("font/IBM_Plex_Mono/IBMPlexMono-Regular.ttf", size)

    @classmethod
    def get_poppins(cls, size=12):
        return cls.get_font("font/Poppins/Poppins-Bold.ttf", size)
