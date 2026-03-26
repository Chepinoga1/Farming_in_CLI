import json
import os

SAVE_FILE = "save.json"
def load_game():
    if not os.path.exists(SAVE_FILE):
        inventory_start = { #Повергнуть балансным правкам не забыть!!!
            "peas": {
                "seeds": 1,
                "crops": 0,
                "time": 10,
                "shop_seeds": 10,
                "cost": 10
            },
            "wheat": {
                "seeds": 1,
                "crops": 0,
                "time": 20,
                "shop_seeds": 10,
                "cost": 20
            },
            "carrot": {
                "seeds": 0,
                "crops": 0,
                "time": 30,
                "shop_seeds": 10,
                "cost": 30
            },
            "cucumber": {
                "seeds": 0,
                "crops": 0,
                "time": 40,
                "shop_seeds": 10,
                "cost": 50
            }
        }
        return {"balance": 100, "fields": [], "inv": inventory_start, "usable_fields": 3, "field_cost": 10, "shop_update_time": 30, "shop_last_update": 0} #время обновление магаза подвергнуть правкам!!!

    with open(SAVE_FILE, "r") as f:
        return json.load(f)


def save_game(data):
    with open(SAVE_FILE, "w") as f:
        json.dump(data, f, indent=4)