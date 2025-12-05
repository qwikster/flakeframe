import configparser
import os
from dataclasses import dataclass
from typing import List

@dataclass
class Asset:
    name: str
    r: int
    g: int
    b: int

@dataclass
class Theme:
    name: str
    author: str
    assets: List[Asset]

class ThemeHandler:
    def __init__(self):
        pass
    
    def create_themefile()
        
    def load_themefile(self, path):
        self.themefile = path
        if not os.path.exist(path):
            self.create_themefile(path)