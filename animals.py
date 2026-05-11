from random import choice as rchoice
import time
from storage import save_game



def buy_goat(data):
    if data['balance'] >= data['animals_cost']['Коза'] and data['buildings_start']['Загон']['availability'] and len(data['animals']) + 1 <= data['buildings_start']['Загон']['slots']:
        name = input('Введите имя козы: ')
        data_goat = {
            'name': name,
            'animal_type': 'Коза',
            'age': 'middle', #small нельзя доить, middle Норм, old старая сдохнет скоро
            'gender': rchoice(['Мужской', 'Женский', 'Женский', 'Женский']),
            'last_milking': 0,
            'to_old': 1209600, #14 дней
            'to_middle': 259200, #3 дня
            'buy_time': time.time() # Время когда куплена взрослая коза, по нему определять старение
        }
        if name in list(data['animals'].keys()):
            print('Это имя уже занято')
            return
        data['animals'][name] = data_goat
        data['balance'] -= data['animals_cost']['Коза']
        print(f'Вы купили козу {name}')
    else:
        print("Нет места в загоне или недостаточно средств")


def aging(data, now):
    for animal in data['animals']:
        if data['animals'][animal]['age'] == 'middle' and data['animals'][animal]['buy_time'] + data['animals'][animal]['to_old'] <= now:
            data['animals'][animal]['age'] = 'old'
            print(f'Ваш(а) {data['animals'][animal]['animal_type']} {data['animals'][animal]['name']} постарел(а)')
        if data['animals'][animal]['age'] == 'small' and data['animals'][animal]['buy_time'] + data['animals'][animal]['to_middle'] >= now:
            data['animals'][animal]['age'] = 'middle'
            print(f'Ваш(а) {data['animals'][animal]['animal_type']} {data['animals'][animal]['name']} повзрослел(а)')
        else:
            pass

def milking(data, choice, now):
    print(range(len(data['animals'])))
    if choice - 1 not in range(len(data['animals'])):
        print('Выбрано несуществующее животное')
        return
    animal = ''
    j = 1
    for i in data['animals']:
        if j == choice:
            animal = i
            break
    print(f'{data['animals'][animal]['animal_type']} {data['animals'][animal]['name']}')
    print(f'Можно покормить: \n 1. требуется 3 гороха. Горох: {data['inv']['горох']['crops']}  \n 2. комбикорм: требуется 2 гороха и 1 овес. В наличии: {data['inv']['горох']['crops']} гороха, {data['inv']['овес']['crops']} овес')
    crop = input('> ')
    if crop == '1' and data['inv']['горох']['crops'] >= 3 and data['animals'][animal]['last_milking'] + 18000 <= now:
        if data['animals'][animal]['age'] == 'small':
            print('Животное еще слишком молодое')
        if data['animals'][animal]['gender'] == 'Мужской':
            print('Вы не можете подоить мужскую особь')
        data['animals'][animal]['last_milking'] = now
        data['inv']['горох']['crops'] -= 3
        data['milks']['Козье молоко']['count'] += 1
        print('Дойка успешна. Следующая через 5 часов')
    elif crop == '2' and data['inv']['горох']['crops'] >= 2 and data['inv']['овес']['crops'] >= 1 and data['animals'][animal]['last_milking'] + 18000 <= now:
        if data['animals'][animal]['age'] == 'small':
            print('Животное еще слишком молодое')
        if data['animals'][animal]['gender'] == 'Мужской':
            print('Вы не можете подоить мужскую особь')
        data['animals'][animal]['last_milking'] = now
        data['inv']['горох']['crops'] -= 2
        data['inv']['овес']['crops'] -= 1
        data['milks']['Козье молоко']['count'] += 2
        print('Дойка успешна. Следующая через 5 часов')
    else:
        print("Недостаточно культуры или врмя дойки еще не пришло")

def dead(data):
    keys = list(data['animals'].keys())
    for animal in keys:
        rand = rchoice([0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
        if data['animals'][animal]['age'] == 'old' and rand == 1:
            data['animals'].pop(animal)
            print(f'Ваш(а) {animal} умер(а)')
            save_game(data)
        if data['animals'][animal]['last_milking'] + 259200 <= time.time():
            data['animals'].pop(animal)
            print(f'Ваш(а) {animal} умер(а) от голода')
            save_game(data)