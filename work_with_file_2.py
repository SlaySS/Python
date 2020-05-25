import sys

if len(sys.argv) < 2:
    print("Необходимо передать рабочую дирекрорию в качестве аргумента командной строки")
    sys.exit()


file_name = sys.argv[1]

f = open('%s' %file_name, mode = "r") # использоват переменную в качестве имени файла
ip_address = []

for line in f:
    # print(line, end='') #end='', не переводить строку
    ip_address.append(line.strip())
# print(work_dir)

print(ip_address)

f.close()