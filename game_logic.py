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
            data["inv"][crop]["seeds"] -= 1
        print(f"Посажено {crop} {count}")
    else:
        print("Недостаточно семян или свободных полей")

def update_shop(data):
    now = int(time.time())
    if now - data["shop_last_update"] >= data["shop_update_time"]:
        for i in range(len(list(data["inv"].keys()))):
            data["inv"][list(data["inv"].keys())[i]]["shop_seeds"] = 10

def update_game(data):
    now = int(time.time())
    ready = []
    ready_bread = []
    for field in data["fields"]:
        if now - field["planted_at"] >= field["grow_time"]:
            ready.append(field)
    for bread in data["bakery"]:
        if now - bread["time_start"] >= bread["time_end"]:
            ready_bread.append(bread)

    def harvest_crop(data, crop):
        data["inv"][crop]["crops"] += 1
        data["inv"][crop]["seeds"] += rchoice([0, 0, 0, 0, 0, 0, 0, 0, 0, 1])

    for field in ready:
        print(f"Выросло: {field["crop"]}")
        data["fields"].remove(field)
        harvest_crop(data, field["crop"])

    for bread in ready_bread:
        print(f"Хлеб готов")
        data["bakery"].remove(bread)
        data["bread"]["Белый хлеб"]['bread']+=1

def buy_seeds(data, crop, count):
    if int(count) <= 0 or int(count) > data["inv"][crop]["shop_seeds"] or data["balance"] < int(count) * data["inv"][crop]["cost"]:
        print("Недостаточно средств или семян в магазине")
        return "stop"
    data["shop_last_update"] = int(time.time())
    data["inv"][crop]["shop_seeds"] -= int(count)
    data["inv"][crop]["seeds"] += int(count)
    data["balance"] -= int(count) * data["inv"][crop]["cost"]
    print(f"Куплено {count} семян {crop}")
    return None

def sell_seeds(data, crop, count):
    if int(count) <= 0 or int(count) > data["inv"][crop]["crops"]:
        print("Невозможное дейтвие")
        return "stop"
    data["inv"][crop]["crops"] -= int(count)
    data["balance"] += int(int(count) * data["inv"][crop]["cost"] * 1.5)
    print(f"Продано {count} культуры {crop}")
    return None

def buy_fields(data, count):
    if int(count) > 0 and int(count) * data["field_cost"] <= data["balance"]:
        data["usable_fields"] += int(count)
        data["balance"] -= int(count) * data["field_cost"]
        print(f"Куплено {count} полей")
        return None
    else:
        print("Недостаточно средств")
        return None
def buy_buildings(data, choice):
    if data["balance"] >= data["buildings_start"][list(data["buildings_start"])[choice]]["build_cost"]:
        #data[choice]["availability"] = True
        data["buildings_start"][list(data["buildings_start"])[choice]]["availability"] = True
        data["balance"] -= data["buildings_start"][list(data["buildings_start"])[choice]]["build_cost"]
    else:
        print("Недостаточно средств")
def sell_bread(data, count, key_bread):
    if int(count) <= 0 or int(count) > data["bread"][key_bread]["bread"]:
        print("Нет такой команды")
        return "stop"
    data["bread"][key_bread]["bread"] -= int(count)
    data["balance"] += (int(count) * data["bread"][key_bread]["cost"])
    print(f"Продано {count} {key_bread}")
    return None

