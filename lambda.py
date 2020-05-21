# def kvadrat(*args):
#     return [x*x for x in args]
#
# spisok = (1,4,5,6,4)
# print(list(map(kvadrat,spisok)))
#
# # функция filter, работает так же как и map, но в качестве функции принимает функцию которая возвращает True или False, и в результат выводит те элементы которые соответствуют True
# def is_adult(age):
#     return age >= 18
# ages = [1,4,56,34,18,17,23]
# list1 = list(filter(is_adult, ages))
# list1.sort()
# print(list1)

test_list = [1, 4, 5, 6, 4, 3, 6]
list2 = list(map((lambda x: x * 3), test_list)) # совместное использование lambda и map

list3 = ([x*5 for x in list2])   # list_comprehesion

print(list(map(lambda x: x/15, list3)))