import time


def plant_crop(data, crop, grow_time):
    data["fields"].append({
        "crop": crop,
        "planted_at": int(time.time()),
        "grow_time": grow_time
    })

    print(f"Planted {crop}")


def update_game(data):
    now = int(time.time())
    ready = []

    for field in data["fields"]:
        if now - field["planted_at"] >= field["grow_time"]:
            ready.append(field)

    for field in ready:
        print(f"Harvested: {field['crop']}")
        data["balance"] += 10
        data["fields"].remove(field)