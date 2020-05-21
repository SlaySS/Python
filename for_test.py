# word = "Paravozzz"
# print(word[4:7:1])
# print(len(word))
# print(word.find('zzz'))

# list = ['paravozz', 'anikina', 'krugalya', 'oko']
# print([x[::-1] for x in list if x == x[::-1]])


# def summa():
#     while True:
#         try:
#             a = int(input('a= '))
#             b = int(input('b= '))
#             print(a + b)
#             break
#         except ValueError as ex:
#             print('Введите число')
#
# summa()


for a, x in enumerate(range(10), 10):
    print(f'{a} значение равно {x}')
