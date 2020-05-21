num = int(input('Введите число : '))
summa = []
for x in range(0, num + 1):
    if x % 3 == 0 or x % 5 == 0:
        summa.append(x)
    else:
        continue
print(summa)
print(sum(summa))