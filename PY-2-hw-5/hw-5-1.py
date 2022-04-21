# 1. Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за четыре квартала для каждого предприятия.
# Программа должна определить среднюю прибыль
# (за год для всех предприятий) и отдельно вывести наименования предприятий,
# чья прибыль выше среднего и ниже среднего.

from collections import OrderedDict, namedtuple

n = int(input('Введите количество фирм:  '))
print()

firms = {}
total = 0
for i in range(n):
    name = input(f'Фирма №{i+1} (название): ')
    profit_1 = float(input(f'Введите прибыль {i+1}-ой фирмы за 1 квартал:  '))
    profit_2 = float(input(f'Введите прибыль {i+1}-ой фирмы за 2 квартал:  '))
    profit_3 = float(input(f'Введите прибыль {i+1}-ой фирмы за 3 квартал:  '))
    profit_4 = float(input(f'Введите прибыль {i+1}-ой фирмы за 4 квартал:  '))
    profit_year = profit_1 + profit_2 + profit_3 + profit_4
    firms[name] = profit_year
    print('\n')
    total += profit_year
print("*" * 50)
print(f'Имеем словарь с данными о фирмах и их годовой прибыли:\n{firms}')

print("*" * 50)
medium_total = round(total / n, 2)
print(f'Средняя прибыль за год для всех фирм: {medium_total}')
print("*" * 50)

firms_medium_profit = {k for k, v in firms.items() if v == medium_total}
print(f'Фирмы с прибылью, РАВНОЙ общей средней прибыли: {firms_medium_profit}')
print()

firms_sort = OrderedDict(sorted(firms.items(), key=lambda x: x[1]))

firms_up = {k for k, v in firms_sort.items() if v <= 0}
print(f'Фирмы без прибыли или же с убытками: {firms_up}')

firms_up = {k for k, v in firms_sort.items() if v > medium_total}
print(f'Фирмы с прибылью БОЛЕЕ общей средней прибыли: {firms_up}')

firms_below = {k for k, v in firms_sort.items() if v < medium_total}
print(f'Фирмы с прибылью МЕНЕЕ общей средней прибыли: {firms_below}')
