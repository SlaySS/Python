#если функция может принимать много значений вида ключ:значение
def price_taxes(**kwargs):
    for x, v in kwargs.items():
        print(f'Поездка {x} стоила {v} рублей')

price_taxes(one=100, two=200)




#если функция может принимать много значений на вход
def calc_taxes(*args):
    for x in args:
        print(f'Got payment = {x}')
    return sum(args) * 0.06

taxes = calc_taxes(6,3,5,87)
print(taxes)

# def printhello(name=''):
#     print(f'Hello {name}')


# def get_sum(a, b):
#     return (a + b)
#
# print(get_sum(10, 5))

# def is_palindrome(word):
#     return word == word[::-1]
# def is_palindrome(word):
#     return word == word[::-1]
# print(is_palindrome('anikina'))
# print(is_palindrome('aabaav'))

# number = list(input('Введите число: '))
# def is_palindrome(number):
#     return number == number[::-1]
#
#
# if is_palindrome(number):
#     print("Palindrom")
# else:
#     print("Not palindrom")