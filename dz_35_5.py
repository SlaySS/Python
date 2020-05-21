list1 = [1, 2, 3, 54, 3, 4, 8, 3, 16]
list2 = [3, 6, 8, 12, 5, 9, 13]

list3 = [n for n in list1 if n % 2 != 0]
list4 = [n for n in list2 if n % 2 == 0]

print(list3 + list4)
