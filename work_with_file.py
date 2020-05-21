file = 'test.txt'
file2 = 'test2.txt'

input_file = open(file, mode='r')
output_file = open(file2, mode='w')

dict = {}

for num, i in enumerate(input_file, 1): # создает нумерованный список начиная с цифры 1
    # stroka = i.split()
    # if '' in i:
    output_file.write(f'В строке : {num} найдена запись {i}')
    # if 'Nika' in i:
    #     dict[stroka[0]] = stroka[1].strip()

input_file.close()
output_file.close()


print(dict)
