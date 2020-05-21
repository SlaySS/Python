x = 0
while x < 10:
    print(f'X = {x}')
    x += 1
else:
    print('X >= 10')


num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sum = 0
for i in num:
    if i % 2 == 0:
        continue
    else:
        sum += i
    if sum > 10:
        break
print(sum)