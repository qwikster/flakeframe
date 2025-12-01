# Main entry point
import sys
import readline
import json
import os
from mapfisher.ui import SettingsUI
from mapfisher.geocode import location_completer, geocode_location

CONFIG_FILE = "config.json"

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return {
        "units_precip": "mm",
        "units_temp": "°C",
        "last_location": None
    }

def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f)
        
def entry():
    config = load_config()
    # etc

if __name__ == "__main__":
    entry()