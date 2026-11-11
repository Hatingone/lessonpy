import math
x_rad = math.radians(int(input('введите число градусов ')))
formula = math.sin(x_rad) + math.cos(x_rad) + math.tan(x_rad)**2
print('значение тригонометрического выражения ', formula)