# x = int(input('Введите количество : '))
# for a in range(x):
#     print('*' * (a + 1))

y = int(input('Введине число : '))
for x in range(0, y + 1):
    if x % 2 == 0:
        print(f'{x} is EVEN')
    else:
        print(f'{x} is ODD')
