weight, height = map(int, input('Введите свой вес и рост: ').split())

calculate_imt = weight / height ** 2

print(f'Ваш индекс массы тела = {calculate_imt * 10000:.1f}')


