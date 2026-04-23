import time

def bakery_usage(data):
    print("\n=== ПЕКАРНЯ  ===")
    print(f"Пшеница: {data["inv"]["пшеница"]['crops']}")
    print("Хлеб делается из трех пшениц")
    print("1. Печь хлеб")
    print("0. Выйти")
    choice = get_input()
    try:
        int(choice)
    except:
        print("Неизвестная команда")
        return
    if choice == "0":
        return
    elif choice == "1":
        print("Сколько?")
        count = get_input()
        try:
            int(count)
        except:
            print("Неизвестная команда")
            return
        if int(data["inv"]["пшеница"]['crops']) >= int(count) * data["bread"]["Белый хлеб"]["cost_index"] and int(count) > 0 and int(count) <= data["buildings_start"]["Пекарня"]["slots"] - len(data["bakery"]):
            for i in range(int(count)):
                data["bakery"].append({
                    "time_start": int(time.time()),
                    "time_end": data["bread"]["Белый хлеб"]["bread_time"]
                })
                data["inv"]["пшеница"]['crops']-=3

            print(f"Пшеницы осталось: {data["inv"]["пшеница"]['crops']}")
            print(f"Будет готово хлеба через 1 час: {count}")
        else:
            print("Пекарня занята или недостаточно культур")

def get_input():
    return input("> ")