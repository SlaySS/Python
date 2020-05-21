palochki = 10
player = 1

print(f'На столе лежат {palochki}')


def end_of_game(sticks):
    return sticks <= 0


def can_take(stiks):
    return stiks >= 1 and stiks <= 3


def switch_player(turn):
    return 1 if turn == 2 else 2


while (not end_of_game(palochki)):
    taken = int(input(f'Игрок {player} введите количество палочек : '))

    if not can_take(taken):
        print('Вы не можете взять меньше 1 или больше 3 палочек')
        continue

    palochki -= taken
    print(f'Взяли {taken} палочек. На столе осталось {palochki}')

    if end_of_game(palochki):
        print(f'Игра закончена. Игрок {player} проиграл.')
        break

    player = switch_player(player)
