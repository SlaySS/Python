import math

point1_x=int(input("Введите координату х точки 1:"))
point1_y=int(input("Введите координату y точки 1:"))
point2_x=int(input("Введите координату х точки 2:"))
point2_y=int(input("Введите координату y точки 2:"))

path = round(math.sqrt((point2_x-point1_x)**2+(point2_y-point1_y)**2),3)

print("Расстояние между точками равно: " + str(path))