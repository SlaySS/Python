import configparser  # импортируем библиотеку

config = configparser.ConfigParser()  # создаём объекта парсера
config.read("config.ini")  # читаем конфиг

print("Hello " + (config["Resources"]["name"]))


file_to_work = (config["Resources"]["file"])

f = open('%s' % file_to_work, mode="r")

ip_address = []

for line in f:
    # print(line, end='') #end='', не переводить строку
    ip_address.append(line.strip())
# print(work_dir)

print(ip_address)

f.close()
