current_hand = [6, 7, 'K', 'A', 9, 8]
card_1 = {2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 0, 8: 0, 9: 0, 10: -1, 'J': -1, 'Q': -1, 'K': -1, 'A': -1}

print(sum(card_1[x] for x in current_hand))