import sys

file = sys.argv[1]

with open(file, mode='r', encoding='utf-8') as open_file:
    line = open_file.readlines()
    for l in line:
        line = "---" + l
        if line.find("aaa") != - 1:
            print(line[::-1], end='')