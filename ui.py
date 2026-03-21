def show_menu(data):
    print("\n=== FARM MENU ===")
    print(f"Balance: {data['balance']}")
    print("1. Plant crops")
    print("2. Inventory")
    print("3. Exit")


def show_plant_menu():
    print("\n=== PLANT MENU ===")
    print("1. Peas (10 sec)")
    print("2. Wheat (20 sec)")
    print("0. Back")

    return input("> ")


def get_input():
    return input("> ")