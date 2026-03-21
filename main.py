import os
from ui import show_menu, get_input, print_inventory
from game_logic import update_game, plant_crop
from storage import load_game, save_game



def handle_choice(choice, data):
    actions = {
        "1": get_crop_choice,
        "2": print_inventory,
        "0": exit}

    action = actions.get(choice)

    if action == get_crop_choice:
        os.system('cls' if os.name == 'nt' else 'clear')
        crop_data = action(data)
        if crop_data == "stop":
            return
        plant_crop(data, crop_data["name"], crop_data["time"])
    elif action == print_inventory:
        action(data)
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
    crops = {}
    for i in range(len(data["inv"])):
        crops[str(i + 1)] = {"name": list(data["inv"])[i], "time": data["inv"][list(data["inv"])[i]]["time"]}
    #crops = {
    #    "1": {"name": data["inv"][1], "time": data["inv"][data["inv"][1]]["time"]},
    #    "2": {"name": data["inv"][2], "time": data["inv"][data["inv"][2]]["time"]},
    #}

    return crops.get(choice)


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