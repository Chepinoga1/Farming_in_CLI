import os
from ui import show_menu, get_input, print_inventory
from game_logic import update_game, plant_crop, buy_seeds
from storage import load_game, save_game



def handle_choice(choice, data):
    actions = {
        "1": get_crop_choice,
        "2": print_inventory,
        "3": shop,
        "0": exit
    }
    action = actions.get(choice)

    if action == get_crop_choice:
        os.system('cls' if os.name == 'nt' else 'clear')
        crop_data = action(data)
        if crop_data == "stop":
            return
        if crop_data == "unknown_command":
            print("Unknown command")
            return
        plant_crop(data, crop_data["name"], crop_data["time"])
    elif action == print_inventory:
        os.system('cls' if os.name == 'nt' else 'clear')
        action(data)
    elif action == shop:
        crop = action(data)
        if crop == "stop":
            return
        if crop == "unknown_command":
            print("Unknown command")
            return
        eror = buy_seeds(data, crop[0]["name"], crop[1])
        if eror == "stop":
            print("Invalid, suka")
    elif action == exit:
        save_game(data)
        action()
    else:
        print("Unknown command")


def get_crop_choice(data):
    from ui import show_plant_menu
    show_plant_menu(data)
    choice = get_input()
    if choice == "0":
        return "stop"
    try:
        int(choice)
    except:
        print("Unknown command")
        return "stop"
    if int(choice) - 1 not in range(len(data["inv"])):
        print("Unknown command")
        return "stop"
    crops = {}
    for i in range(len(data["inv"])):
        crops[str(i + 1)] = {"name": list(data["inv"])[i], "time": data["inv"][list(data["inv"])[i]]["time"]}
    return crops.get(choice)

def shop(data):
    from ui import print_shop
    print("\n=== What would you like to do? ===")
    print("1. Buy seeds")
    print("2. Sell crops")
    print("0. Back")
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
            print("Unknown command")
            return "stop"
        if int(choice) - 1 not in range(len(data["inv"])):
            print("Unknown command")
            return "stop"
        crops = {}
        for i in range(len(data["inv"])):
            crops[str(i + 1)] = {"name": list(data["inv"])[i]}
        print("How many?")
        count = input("> ")
        try:
            int(count)
        except:
            print("Unknown command")
            return "stop"
        return crops.get(choice), count

    elif choice == "2":
        print("Coming soon")
        return "stop"
    else :
        print("Unknown command")
        return "stop"


def main():
    data = load_game()

    while True:
        update_game(data)
        show_menu(data)

        choice = get_input()
        handle_choice(choice, data)

        save_game(data)


if __name__ == "__main__":
    main()