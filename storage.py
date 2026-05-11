import json
import os

SAVE_FILE = "save.json"
def load_game():
    if not os.path.exists(SAVE_FILE):
        print('Спасибо за участие бета тестировании')
        print('Более подробную информацию читайте на GiHub пректа')
        inventory_start = { #Повергнуть балансным правкам не забыть!!!
            "горох": {
                "seeds": 1,
                "crops": 0,
                "time": 60,
                "shop_seeds": 10,
                "cost": 10
            },
            "пшеница": {
                "seeds": 1,
                "crops": 0,
                "time": 120,
                "shop_seeds": 10,
                "cost": 20
            },
            "овес": {
                "seeds": 0,
                "crops": 0,
                "time": 150,
                "shop_seeds": 10,
                "cost": 30
            },
            "морковь": {
                "seeds": 0,
                "crops": 0,
                "time": 18000,
                "shop_seeds": 10,
                "cost": 100
            },
            "огурец": {
                "seeds": 0,
                "crops": 0,
                "time": 18000,
                "shop_seeds": 10,
                "cost": 100
            }
        }
        items = {
            'bread': {
                "Белый хлеб": {
                    'bread': 0,
                    'cost_index': 3, #стоимость приготовления в культуре
                    "bread_time": 3600,
                    "cost": 150
                }
            },
            'milks': {
            'Козье молоко': {'count': 0, 'cost': 120}
            }
        }
        animals_cost = {
            "Коза": 1000
        }
        buildings_start = {
            "Пекарня": {
                "availability": False,
                "build_cost": 200,
                "slots": 10

            },
            "Загон": {
                "availability": False,
                "build_cost": 10000,
                "slots": 10,

            }
        }

        animals = {}
        return {"balance": 100, "fields": [], "bakery": [], "inv": inventory_start, "items": items,"buildings_start": buildings_start, "usable_fields": 3, "field_cost": 100, "shop_update_time": 86400, "shop_last_update": 0, 'animals': animals, 'animals_cost': animals_cost} #время обновление магаза подвергнуть правкам!!!

    with open(SAVE_FILE, "r") as f:
        return json.load(f)


def save_game(data):
    with open(SAVE_FILE, "w") as f:
        json.dump(data, f, indent=4)