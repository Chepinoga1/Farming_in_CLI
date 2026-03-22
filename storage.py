import json
import os

SAVE_FILE = "save.json"
def load_game():
    if not os.path.exists(SAVE_FILE):
        inventory_start = {
            "peas": {
                "seeds": 1,
                "crops": 0,
                "time": 10
            },
            "wheat": {
                "seeds": 1,
                "crops": 0,
                "time": 20
            }
        }
        return {"balance": 100, "fields": [], "inv": inventory_start}

    with open(SAVE_FILE, "r") as f:
        return json.load(f)


def save_game(data):
    with open(SAVE_FILE, "w") as f:
        json.dump(data, f, indent=4)