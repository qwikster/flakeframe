import configparser
import os
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Asset:
    name: str
    r: int
    g: int
    b: int
    fg: Optional[bool]

@dataclass
class Theme:
    name: str
    author: str
    assets: List[Asset]

class ThemeHandler:
    def __init__(self, default_theme =
                    Theme(name = "default", author = "qwik", assets = [
                        Asset(name = "fore", r=255, g=255, b=255, fg=True), Asset(name = "back", r=16, g=16, b=16, fg=False)
                    ]
                )):
        
        self.storage = configparser.ConfigParser() # should never be actually read except when loading from
        self.default_theme = default_theme
        self.current: str
        self.themes: List[Theme] = []
            
    def save(self):
        # load from configfile format to usable OOP
        if not hasattr(self, "themefile"):
            raise RuntimeError("Attempted to save themes before savefile was picked, use load_savefile(path) first.")
        
        for theme in self.themes:
            self.storage[theme.name] = {
                "name": theme.name,
                "author": theme.author,
            }
            for asset in theme.assets:
                self.storage[theme.name][asset.name] = f"{asset.r}, {asset.g}, {asset.b}, {str(asset.fg)}"
        
        with open(self.themefile, "w") as themefile:
            self.storage.write(themefile)
    
    def load(self):
        if not hasattr(self, "themefile"):
            raise RuntimeError("Attempted to load themes before savefile was picked, use load_savefile(path) first (or probably instead).")

        self.storage = configparser.ConfigParser() # CLEAR
        self.storage.read(self.themefile)
        for th in self.storage.sections():
            if th == "DEFAULT":
                self.current = self.storage["DEFAULT"]["current_theme"]
                continue
            for i in self.storage[th]:
                print(self.storage[th][i])
            input() # WORK ON PARSING LOGIC FOR LOAD FROM FILE
     
    
    def new_theme(self, theme):
        self.themes.append(Theme)
    
    def create_themefile(self, path):
        self.storage["DEFAULT"]["current_theme"] = "default"
        self.new_theme(self.default_theme)
        self.save()
    
    def get_termcol(self, asset: Asset) -> str:
        # fg: \x1b[38;2;r;g;bm
        # bg: \x1b[48;2;r;g;bm
        bg = "38" if asset.fg else "48"
        return f"\x1b[{bg};2;{asset.r};{asset.g};{asset.b}"
    
    def load_themefile(self, path):
        self.themefile = path
        if not os.path.exists(path):
            self.create_themefile(path)
        self.load()
        print("work")
        input()