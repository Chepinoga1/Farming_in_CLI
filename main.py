
import os
from ui import show_menu, get_input
from game_logic import update_game, plant_crop
from storage import load_game, save_game



def handle_choice(choice, data):
    actions = {
        "1": get_crop_choice,
        "2": print_inventory,
        "3": exit}

    action = actions.get(choice)

    if action == get_crop_choice:
        os.system("cls")
        crop_data = action()
        plant_crop(data, crop_data["name"], crop_data["time"])
    elif action == print_inventory:
        action(data)
    elif action == exit:
        action()
    else:
        print("Unknown command")


def get_crop_choice():
    from ui import show_plant_menu

    choice = show_plant_menu()

    crops = {
        "1": {"name": "peas", "time": 10},
        "2": {"name": "wheat", "time": 20},
    }

    return crops.get(choice)


def print_inventory(data):
    print("\n=== INVENTORY ===")
    print(f"Balance: {data['balance']}")
    print(f"Active fields: {len(data['fields'])}")


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