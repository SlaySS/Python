import re

import sys

if len(sys.argv) == 1:
    print('Не заданы аргументы')
    sys.exit(2)

file = sys.argv[1]
data = open(file, mode='r', encoding='utf-8')

for line in data:
    a = line.replace(' ', '')
    print(a.strip())