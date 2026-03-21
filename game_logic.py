import time
from random import choice as rchoice

def plant_crop(data, crop, grow_time):
    data["fields"].append({
        "crop": crop,
        "planted_at": int(time.time()),
        "grow_time": grow_time
    })
    data["inv"][crop]["seeds"] -=1
    print(f"Planted {crop}")


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

