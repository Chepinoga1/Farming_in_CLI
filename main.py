import os
from ui import show_menu, get_input, print_inventory, print_shop_sell, print_shop_fields, print_buildings_menu, print_shop_sell_for_all, print_buy_buildings_menu
from game_logic import update_game, plant_crop, buy_seeds, sell_seeds, buy_fields, update_shop, buy_buildings, sell_bread
from storage import load_game, save_game
from usage import bakery_usage



def handle_choice(choice, data):
    actions = {
        "1": get_crop_choice,
        "2": print_inventory,
        "3": shop,
        "4": print_buildings_menu,
        "0": exit
    }
    action = actions.get(choice)

    if action == get_crop_choice:
        os.system('cls' if os.name == 'nt' else 'clear')
        crop_data = action(data)
        if crop_data == "stop":
            return
        if crop_data == "unknown_command":
            print("Неизвестная команда")
            return
        print("Сколько?")
        count = get_input()
        plant_crop(data, crop_data["name"], crop_data["time"], count)
    elif action == print_inventory:
        os.system('cls' if os.name == 'nt' else 'clear')
        action(data)
    elif action == shop:
        crop = action(data)
        if crop == "stop":
            return
        if crop == "unknown_command":
            print("Неизвестная команда")
            return
    elif action == print_buildings_menu:
        action(data)
        choice = get_input()
        if choice == "1" and data["buildings_start"]["Пекарня"]["availability"]:
            bakery_usage(data)


    elif action == exit:
        save_game(data)
        action()
    else:
        print("Неизвестная команда")


def get_crop_choice(data):
    from ui import show_plant_menu
    show_plant_menu(data)
    choice = get_input()
    if choice == "0":
        return "stop"
    try:
        int(choice)
    except:
        print("Неизвестная команда")
        return "stop"
    if int(choice) - 1 not in range(len(data["inv"])):
        print("Неизвестная команда")
        return "stop"
    crops = {}
    for i in range(len(data["inv"])):
        crops[str(i + 1)] = {"name": list(data["inv"])[i], "time": data["inv"][list(data["inv"])[i]]["time"]}
    return crops.get(choice)

def shop(data):
    from ui import print_shop
    print("\n=== Что бы вы хотели сделать? ===")
    print("1. Купить семена")
    print("2. Продать культуры")
    print("3. Купить новые поля")
    print("4. Построить здания")
    print("5. Продать продукцию")
    print("0. Выйти")
    choice = get_input()
    if choice == "0":
        return "stop"
    elif choice == "1":
        print_shop(data)
        choice = get_input()
        if choice == "0":
            return "stop"
        try:
            int(choice)
        except:
            print("Неизвестная команда")
            return "stop"
        if int(choice) - 1 not in range(len(data["inv"])):
            print("Неизвестная команда")
            return "stop"
        crops = {}
        for i in range(len(data["inv"])):
            crops[str(i + 1)] = {"name": list(data["inv"])[i]}
        print("Сколько?")
        count = input("> ")
        try:
            int(count)
        except:
            print("Неизвестная команда")
            return
        #return crops.get(choice), count
        buy_seeds(data, crops.get(choice)["name"], count)

    elif choice == "2":
        print_shop_sell(data)
        choice = get_input()
        if choice == "0":
            return "stop"
        try:
            int(choice)
        except:
            print("Неизвестная команда")
            return "stop"
        if int(choice) - 1 not in range(len(data["inv"])):
            print("Неизвестная команда")
            return "stop"
        crops = {}
        for i in range(len(data["inv"])):
            crops[str(i + 1)] = {"name": list(data["inv"])[i]}
        print("Сколько?")
        count = input("> ")
        try:
            int(count)
        except:
            print("Неизвестная команда")
            return "stop"

        sell_seeds(data, crops.get(choice)["name"], count)
    elif choice == "3":
        print_shop_fields(data)
        choice = get_input()
        if choice == "0":
            try:
                int(choice)
            except:
                print("Неизвестная команда")
                return "stop"
            return "stop"
        if choice == "1":
            print("Сколько?")
            count = input("> ")
            try:
                int(count)
            except:
                print("Неизвестная команда")
                return "stop"
            buy_fields(data, int(count))
    elif choice == "4":
        print_buy_buildings_menu(data)
        choice = get_input()
        if choice == "1":
            try:
                int(choice)
            except:
                print("Неизвестная команда")
                return "stop"
            buy_buildings(data, (int(choice) - 1))
    elif choice == '5':
        print_shop_sell_for_all(data)
        choice = get_input()
        if choice == "0":
            return "stop"
        try:
            int(choice)
        except:
            print("Неизвестная команда")
            return "stop"
        if int(choice) - 1 not in range(len(data["bread"])):
            print("Неизвестная команда")
            return "stop"
        bread_inv = {}
        for i in range(len(data["bread"])):
            bread_inv[str(i + 1)] = {"name": list(data["bread"])[i]}
            print("Сколько?")
            count = get_input()
            try:
                int(count)
            except:
                print("Неизвестная команда")
                return "stop"
            sell_bread(data, count, bread_inv.get(choice)["name"])
    else :
        print("Неизвестная команда")
        return "stop"


def main():
    data = load_game()

    while True:
        update_game(data)
        update_shop(data)
        show_menu(data)

        choice = get_input()
        handle_choice(choice, data)

        save_game(data)


if __name__ == "__main__":
    main()