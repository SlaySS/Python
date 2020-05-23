# тоже рабочий вариантб но второй лучше
# def check_sequence(lst):
#     unic = max([lst.count(x) for x in lst])
#     print(unic)
#     if lst == sorted(lst) and unic == 1:
#         return 1
#     if lst == sorted(lst, reverse=True) and unic == 1:
#         return -1
#     else:
#         return 0

#второй вариант
def check_sequence(lst):
    if lst == sorted(set(lst)):
        return 1
    if lst == sorted(set(lst), reverse=True):
        return -1
    else:
        return 0

lst1 = [1, 2, 3, 4, 5]
lst2 = [1, 2, 3, 5, 4]
lst3 = [5, 4, 3, 2, 1]
lst4 = [1, 1, 3]

print(lst1)

print(check_sequence(lst4))
