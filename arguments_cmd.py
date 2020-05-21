import os
import sys

if len(sys.argv) < 2:
    print('Задайте аргументы запуска!')
else:
    print(sys.argv[1] + ' ' + sys.argv[2])


os.system('systeminfo')