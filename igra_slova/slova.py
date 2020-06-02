filename = 'original.csv'
dict = []
with open(filename, mode='r') as file:
    for line in file:
        dict.append(line.split(','))

# dict = [name.strip() for name in dict]


print(dict)
