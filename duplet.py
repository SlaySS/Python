# def calc_dice_scores(lst):
#     return sum([a + b for a, b in lst]) if not any([a == b for a, b in lst]) else 0
#
#
# popytka1 = [(3, 5), (5, 3), (4, 6)]
#
# print(calc_dice_scores(popytka1))


def any_duplicates(square):
    plain = [i for x in square for i in x]
    return sorted(plain) != [1, 2, 3, 4, 5, 6, 7, 8, 9]


print(any_duplicates([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
