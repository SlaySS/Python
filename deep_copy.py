# глубокое и поверхностное копирование
list1 = [1, 2, 3, [5, 6, 7]]
print(list1)
list2 = list1.copy()
list2[3].append(8)
print(list1)
print(list2)
#как видно, 8-ка добавилась в оба листа, так как команда copy не копирует внутреннее состояние
#объекта, а копирует тольео ссылку на него

import copy
list3=copy.deepcopy(list1)
list3[3].append(9)
print(list1)
print(list3)


