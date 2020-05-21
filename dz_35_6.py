table_cards = ['A_S', 'J_H', '7_D', '8_D', '10_D']
hand_cards = ['J_D', '3_D']

table_suits = [i[-1] for i in table_cards]
hands_suit = [i[-1] for i in hand_cards]

all_cards = table_suits + hands_suit
print(all_cards.count('S'))

flush = any([all_cards.count(suit) >= 5 for suit in 'SCHD'])

if flush:
    print('Flush!')
else:
    print('No Flush!')

#
# S = 0
# H = 0
# D = 0
# C = 0
#
# for card in all_cards:
#     if card[-1] == 'S':
#         S += 1
#     if card[-1] == 'C':
#         C += 1
#     if card[-1] == 'D':
#         D += 1
#     if card[-1] == 'H':
#         H += 1
#
#
#
# if C >= 5 or S >= 5 or D >= 5 or H >= 5:
#     print('Flush!')
# else:
#     print('No Flush!')
#
# print(f'S = {S}')
# print(f'C = {C}')
# print(f'H = {H}')
# print(f'D = {D}')
