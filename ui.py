def show_menu(data):
    print("\n=== FARM MENU ===")
    print(f"Balance: {data['balance']}")
    print("1. Plant crops")
    print("2. Inventory")
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
        if data["inv"][list(data["inv"])[i]]["seeds"] !=0:
            print(f"Name: {list(data["inv"].keys())[i]}, Crops: {data["inv"][list(data["inv"].keys())[i]]['crops']}, Seeds: {data["inv"][list(data["inv"].keys())[i]]['seeds']}")




def get_input():
    return input("> ")