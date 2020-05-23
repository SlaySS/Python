# izmeneniya vetka2

def log_function(func):
    def wrap():
        print(f'Start {func}')
        func()
        print(f'End {func}')

    return wrap


week = {
    "понедельник": 1,
    "вторник": 2,
    "среда": 3,
    "четверг": 4,
    "пятница": 5,
    "суббота": 6,
    "воскресенье": 7,
}


@log_function
def print_day():
    print([day for day in week.keys()])


stih = ("У попа была собака, он ее любил. Она съела кусок мяса, он ее убил")
stih_list = stih.split(" ")
stih_list = [slovo.strip(".") for slovo in stih_list]
stih_list = [slovo.strip(",") for slovo in stih_list]
stih_list = [slovo.lower() for slovo in stih_list]

print(stih_list)
