from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

d1 = date(2020, 5, 11)
print(d1)
print(d1.year)
print(d1.month)
print(d1.day)

t1 = time(8, 41, 10)
print(t1)
print(t1.hour)
print(t1.minute)
print(t1.second)

print("Сегодня " + str(date.today()))

dt = datetime(2020, 5, 11, 8, 46, 10)
dt_today = datetime.today()
print(dt)
print(dt_today)
print(datetime.today().day, datetime.today().hour)

dt = datetime(2020, 5, 11, 8, 46, 10)
dt_new = dt.replace(hour=9)
print(dt_new)

# как отпарсить время из входной строки
dt = datetime.strptime("30/08/2018", "%d/%m/%Y")
print(dt)

dt = datetime.strptime("29/03/2018 10:44", "%d/%m/%Y %H:%M")
print(dt)

dt = datetime.strptime("06-28-18 09:20", "%m-%d-%y %H:%M")
print(dt)

dt = datetime.strptime("2020-05-11 09:20", "%Y-%m-%d %H:%M")
print(dt)
print(dt.strftime("%Y %B %d число (%A)"))

# можно производить операции
iam = date(1978, 5, 9)
jenya = date(1981, 12, 19)
print(iam - jenya)
