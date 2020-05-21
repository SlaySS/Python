numbers = [1, 2, 3, 4, 5]
for i in numbers:
    print(i)

# Обращение по индексу, можно выполнять действия со значениями, в данном случае изменить их на квадраты самих себя
numbers = [1, 2, 3, 4, 5]
for i, item in enumerate(numbers):
    numbers[i] **= 2
print(numbers)
# если не хоим создавать именованную переменную то можно использовать символ "_"
for _ in "Slava":
    print(_)

# пробежаться по списку кортежей
person = [('Slava', 41), ('Jenya', 39), ('Nika', 11)]
for (name, age) in person:
    print(f'{name} is {age} years old')

# вложенные циклы
list1 = [1, 3, 5, -3, -7, 4, 0]
list2 = [0, 3, -3, -4, 7, 9]
list3 = [-1, -2, -7, -1, 0, -9]
sum = [];
for x in list1:
    for y in list2:
        for z in list3:
            if x + y + z == 0:
                sum.append((x,y,z))
print(sum)

# list comprehesion
numbers = [n*n for n in range(1,11)]
print(numbers)

# можно вставлять условие
numbers = [n*n for n in range(1,11) if n%2==0] # если четные значения (делится без остатка на 2)
print(numbers)

