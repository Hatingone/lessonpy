USD_TO_RUB = 95.50

def convert_usd_to_rub(amount_usd):
    return amount_usd * USD_TO_RUB
    '''возвращает сумму после конвертации валют'''

amount_usd = int(input('Введите количество долларов: '))
allready_calculated = convert_usd_to_rub(amount_usd)

print(f'Сумма рублей после конвертации валют = {allready_calculated}')

