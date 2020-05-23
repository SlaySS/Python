legs = {
    'cat': 4,
    'chicken': 2,
    'olov_soldier': 1
}

month = dict(january=31, febrary=28, march=31)

# получение значения по ключу
# вариант 1
nogi = legs['cat']
print(f"У кошки {nogi} ноги")
# вариант 2
nogi = legs.get('cat')

# Добавить запись
legs['cow'] = 4

# Поменять значение записи
legs['cow'] = 5

# Удалить запись
del legs['cow']

# Список ключей словаря
list(legs.keys())

# Список значений словаря
print(list(legs.values()))

# Сортировка ключей
print(sorted(legs.keys()))

# Поиск в словаре
# есть ли ?
print('dog' in legs)
# нет ли?
print('dog' not in legs)

# цикл для словаря
for k, v in legs.items():
    print(k, v)

##-------tuple Кортежи (неизменяемые списки)-------------
#объявление так же как list, но скобки круглые
person = ('Nika', 'Papa', 'Mama')
print(len(person))
print(person[2])


