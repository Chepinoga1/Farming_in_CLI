def show_menu(data):
    print("\n=== FARM MENU ===")
    print(f"Balance: {data['balance']}")
    print("1. Plant crops")
    print("2. Inventory")
    print("3. Shop")
    print("0. Exit")


def show_plant_menu(data):
    print("\n=== PLANT MENU ===")
    for i in range((len(data["inv"]))):
        if data["inv"][list(data["inv"])[i]]["seeds"] != 0:
            print(f"{i + 1}. {list(data["inv"].keys())[i]} Time ({data["inv"][list(data["inv"].keys())[i]]['time']}s)")
    print("0. Back")


def print_inventory(data):
    print("\n=== INVENTORY ===")
    print(f"Balance: {data['balance']}")
    print(f"Active fields: {len(data['fields'])}")
    for i in range((len(data["inv"]))):
        if data["inv"][list(data["inv"])[i]]["seeds"] !=0 or data["inv"][list(data["inv"])[i]]["crops"] != 0:
            print(f"Name: {list(data["inv"].keys())[i]}, Crops: {data["inv"][list(data["inv"].keys())[i]]['crops']}, Seeds: {data["inv"][list(data["inv"].keys())[i]]['seeds']}")

def print_shop(data):
    print("\n=== SHOP ===")
    print(f"Balance: {data['balance']}")
    for i in range((len(data["inv"]))):
        print(f"{i + 1}. Name: {list(data["inv"].keys())[i]}, Seeds: {data["inv"][list(data["inv"].keys())[i]]['shop_seeds']}, In inventory: {data["inv"][list(data["inv"].keys())[i]]['seeds']}, Cost: {data['inv'][list(data["inv"].keys())[i]]['cost']}")
    print("0. Back")

def print_shop_sell(data):
    print("\n=== SHOP ===")
    print(f"Balance: {data['balance']}")
    for i in range((len(data["inv"]))):
        print(f"{i + 1}. Name: {list(data["inv"].keys())[i]}, Crops: {data["inv"][list(data["inv"].keys())[i]]['crops']}, Cost: {int(data['inv'][list(data["inv"].keys())[i]]['cost'] * 1.5)}")
    print("0. Back")

def print_shop_fields(data):
    print("\n=== SHOP ===")
    print(f"Balance: {data['balance']}")
    print("Well, 1 Field cost 10")
    print ("1. Buy field")
    print("0. Back")

def get_input():
    return input("> ")