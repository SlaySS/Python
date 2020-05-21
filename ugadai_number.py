import random

num = random.randint(1, 50)
print(num)
a = 0
popitki = 6

while popitki > 0:
    print(f'У вас еще есть {popitki} попыток')
    a = int(input('Введите число от 1 до 50 :'))
    popitki -= 1
    if a > num and popitki > 0:
        print("Ваше число больше загаданного! Попробуйте еще раз. ")
        continue
    if a < num and popitki > 0:
        print("Ваше число меньше загаданного! Попробуйте еще раз. ")
        continue
    if popitki == 0:
        print("Вы не уложились в 6 попыток!")
        break
    if a == num:
        print("Поздравляю вы угадали!!!")
        break


