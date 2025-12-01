import sys
import shutil
from mapfisher.input import read_key
from mapfisher.geocode import suggest_locations

BOX_WIDTH = 60
BOX_HEIGHT = 12

COLOR_RESET = "\x1b[0m"
COLOR_HIGHLIGHT = "\x1b[47;30m"
COLOR_SELECTED = "\x1b[42;30m"
COLOR_PROMPT = "\x1b[34m"

def clear():
    sys.stdout.write("\x1b[2j\x1b[H")
    sys.stdout.flush()

def get_terminal_size():
    return shutil.get_terminal_size((80, 24))

class SettingsUI:
    def __init__(self, config):
        self.options = [
            {"name": "precip", "label": "Distance Units"   , "states": ["mm", "inch"], "value": config["units_precip"]},
            {"name": "temp"  , "label": "Temperature Units", "states": ["°C", "°F"  ], "value": config["units_temp"]},
            {"name": "search", "label": "Search Locations" , "states": None          , "value": None},
            {"name": "quit"  , "label": "Quit..."          , "states": None          , "value": None},
        ]
        self.current_option = 0
        self.search_mode = False
        self.search_input = ""
        self.suggestions = []
        self.selected_sugg = 0
    
    def draw_ui(self):
        clear()
        lines = [
            "Settings",
            ""
        ]
        
    def run(self):
        self.draw_ui()
        
        while True:
            key = read_key()
    
    def toggle_state(self, direction):
        opt = self.options[self.current_option]
        
    def update_suggestions(self):
        self.suggestions = suggest_locations(self.search_input)
        self.selected_sugg = 0
        
def draw_box(lines):
    term_width, term_height = get_terminal_size()
    