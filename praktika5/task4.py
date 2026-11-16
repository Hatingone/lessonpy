import math

def calculate_rectangle_area(width, height):
    return width * height

def calculate_circle_area(radius):
    return math.pi * radius ** 2

width = int(input('Введите ширину прямоугольника: '))
height = int(input('Введите высоту прямоугольника: '))
radius = int(input('Введите радиус круга: '))

calculated_rectangle_area = calculate_rectangle_area(width, height)
print(f'Площадь прямоугольника равна: {calculated_rectangle_area} см')
calculated_circle_area = calculate_circle_area(radius)
print(f'Площадь круга равна: {calculated_circle_area} см')

