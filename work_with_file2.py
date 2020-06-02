file = 'test.txt'

with open(file, mode='r', encoding='utf-8') as open_file:
    line = open_file.read()
    print(line)
  