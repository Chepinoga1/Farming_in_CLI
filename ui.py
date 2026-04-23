def show_menu(data):
    print("\n=== ГЛАВНОЕ МЕНЮ ===")
    print(f"Баланс: {data['balance']}")
    print("1. Посадить семена")
    print("2. Инвентарь")
    print("3. Магазин")
    print("4. Твои постройки")
    print("0. Сохраниться и выйти")


def show_plant_menu(data):
    print("\n=== МЕНЮ ПОСАДКИ ===")
    for i in range((len(data["inv"]))):
        if data["inv"][list(data["inv"])[i]]["seeds"] != 0:
            print(f"{i + 1}. {list(data["inv"].keys())[i]}")# Время ({data["inv"][list(data["inv"].keys())[i]]['time']}s)")
    print("0. Выйти")


def print_inventory(data):
    print("\n=== ИНВЕНТАРЬ ===")
    print(f"Баланс: {data['balance']}")
    print(f"Все поля: {data["usable_fields"]}, Активные поля: {len(data['fields'])}, Доступно: {data["usable_fields"] - len(data['fields'])}")
    for i in range((len(data["inv"]))):
        if data["inv"][list(data["inv"])[i]]["seeds"] !=0 or data["inv"][list(data["inv"])[i]]["crops"] != 0:
            print(f"Название: {list(data["inv"].keys())[i]}, Культуры: {data["inv"][list(data["inv"].keys())[i]]['crops']}, Семена: {data["inv"][list(data["inv"].keys())[i]]['seeds']}")
    #bakery part
    if data['buildings_start']['Пекарня']['availability'] == True:
        print(f'Рабочие ячейки пекарни: {len(data["bakery"])}')
        for i in range((len(data["bread"]))):
            if data['bread'][list(data["bread"].keys())[i]]["bread"] != 0:
                print(f"Название: {list(data["bread"].keys())[i]}, Количество: {data['bread'][list(data["bread"].keys())[i]]["bread"]}")
def print_shop(data):
    print("\n=== МАГАЗИН ===")
    print(f"Баланс: {data['balance']}")
    for i in range((len(data["inv"]))):
        print(f"{i + 1}. Название: {list(data["inv"].keys())[i]}, Семена: {data["inv"][list(data["inv"].keys())[i]]['shop_seeds']}, В инвентаре: {data["inv"][list(data["inv"].keys())[i]]['seeds']}, Стоимость: {data['inv'][list(data["inv"].keys())[i]]['cost']}")
    print("0. Выйти")

def print_shop_sell(data):
    print("\n=== МАГАЗИН ===")
    print(f"Баланс: {data['balance']}")
    for i in range((len(data["inv"]))):
        print(f"{i + 1}. Название: {list(data["inv"].keys())[i]}, Культуры: {data["inv"][list(data["inv"].keys())[i]]['crops']}, Стоимость: {int(data['inv'][list(data["inv"].keys())[i]]['cost'] * 1.5)}")
    print("0. Back")
#для всего, для доп элементов добавлять параметры в новый for
def print_shop_sell_for_all(data):
    print("\n=== МАГАЗИН ===")
    print(f"Баланс: {data['balance']}")
    for i in range((len(data["bread"]))):
        print(f"{i + 1}. Название: {list(data["bread"].keys())[i]}, Количество: {data["bread"][list(data["bread"].keys())[i]]["bread"]}")

def print_shop_fields(data):
    print("\n=== МАГАЗИН ===")
    print(f"Баланс: {data['balance']}")
    print("Каждое поле стоит 100")
    print ("1. Купить поля")
    print("0. Выйти")

def print_buildings_menu(data):
    print("\n=== ЗДАНИЯ ===")
    for i in range((len(data["buildings_start"]))):
        if data["buildings_start"][list(data["buildings_start"].keys())[i]]["availability"]:
            print(f"{i +1}. Использовать здание {list(data["buildings_start"].keys())[i]}")
    not_in_range = []
    for i in range((len(data["buildings_start"]))):
        if data["buildings_start"][list(data["buildings_start"].keys())[i]]["availability"] == True:
            not_in_range.append(list(data["buildings_start"].keys())[i])
    if not_in_range == []:
        print("Зданий еще нет. Сначала их необходимо построить")
        return "stop"

def print_buy_buildings_menu(data):
    print("\n=== ПОСТРОЙКА ===")
    for i in range((len(data["buildings_start"]))):
        if data["buildings_start"][list(data["buildings_start"].keys())[i]]["availability"] == False:
            print(f"{i + 1}. Приобрести здание {list(data["buildings_start"].keys())[i]}")
    print('0. Выйти')
def get_input():
    return input("> ")