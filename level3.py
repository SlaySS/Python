# Создание
names=["John", "Petya", "Jim", "Stive"]
# заменить элемент
names[0]="Petya"
# добававить элемент
names.append("Ivan")
# удалить последний элемент, если указать индекс элемента то удалится элемент с указанным индексом
names.pop()
# сортировка
names.sort()
# сортировка по ключу, по длине
names.sort(key=len)
# реверсировать список
names.reverse()

print(names)
print(names.count("Petya"))

names = [name.upper() for name in names]


print(names)
print(names.count("Petya"))