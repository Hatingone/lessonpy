NALOG_STAVKA = 0.13

dohod_godovoi = int(input('Введите свой доход: '))

sum_nalog = dohod_godovoi * NALOG_STAVKA
itog_dohod = dohod_godovoi - sum_nalog

print(f'Ваш итоговый налог равен = {itog_dohod:.2f} рублей, а сумма налога = {sum_nalog:.2f} рублей')