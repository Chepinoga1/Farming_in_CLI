import time
from random import choice as rchoice

def plant_crop(data, crop, grow_time, count):
    if data["inv"][crop]["seeds"] >= int(count) and int(count) <= data["usable_fields"] - len(data["fields"]):
        for i in range(int(count)):
            data["fields"].append({
                "crop": crop,
                "planted_at": int(time.time()),
                "grow_time": grow_time
            })
            data["inv"][crop]["seeds"] -=1
        print(f"Planted {crop} {count}")
    else:
        print("No seeds = no crops, stupid")


def update_game(data):
    now = int(time.time())
    ready = []

    for field in data["fields"]:
        if now - field["planted_at"] >= field["grow_time"]:
            ready.append(field)

    def harvest_crop(data, crop):
        data["inv"][crop]["crops"] += 1
        data["inv"][crop]["seeds"] += rchoice([0, 0, 0, 0, 0, 0, 0, 0, 0, 1])

    for field in ready:
        print(f"Harvested: {field['crop']}")
        data["fields"].remove(field)
        harvest_crop(data, field["crop"])

def buy_seeds(data, crop, count):
    if int(count) <= 0 or int(count) > data["inv"][crop]["shop_seeds"] or data["balance"] < int(count) * data["inv"][crop]["cost"]:
        return "stop"
    data["inv"][crop]["shop_seeds"] -= int(count)
    data["inv"][crop]["seeds"] += int(count)
    data["balance"] -= int(count) * data["inv"][crop]["cost"]
    print(f"Buying {count} seeds {crop}")
    return None

def sell_seeds(data, crop, count):
    if int(count) <= 0 or int(count) > data["inv"][crop]["crops"]:
        print("Invalid, suka!")
        return "stop"
    data["inv"][crop]["crops"] -= int(count)
    data["balance"] += int(int(count) * data["inv"][crop]["cost"] * 1.5)
    print(f"Selling {count} crops {crop}")
    return None

def buy_fields(data, count):
    if int(count) > 0 and int(count) * data["field_cost"] <= data["balance"]:
        data["usable_fields"] += int(count)
        data["balance"] -= int(count) * data["field_cost"]
        print(f"Buying {count} fields")
        return None
    else:
        print("Deneg net, sosi hui")
        return None