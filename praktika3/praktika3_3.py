
try:
    num1 = int(input('введите число: '))
    num2 = int(input('введите число: '))
    print(num1 + num2)
except ValueError:
    print('надо ввести целое число')

