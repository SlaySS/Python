board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def board_draw(state):
    for x, y in enumerate(state):
        if (x + 1) % 3 == 0:
            print(f'{y}')
        else:
            print(f'{y}|', end='')


winner_combination = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),
                      (0, 4, 8), (2, 4, 6)]


def get_winner(state, combinations):
    for x, y, z in combinations:
        if state[x] == state[y] and state[y] == state[z] and (state[x] == 'X' or state[x] == 'O'):
            return state[x]
    return ''


def play_game(board):
    current_sign = 'X'
    while(get_winner(board, winner_combination) == ''):
        index = int(input(f'В какую клеточку поставить {current_sign}?'))
        board[index] = current_sign
        board_draw(board)

        winner_sign = get_winner(board, winner_combination)
        if winner_sign != '':
            print(f'Победил игрок {winner_sign} !!!')

        current_sign = 'X' if current_sign == 'O' else 'O'


play_game(board)
