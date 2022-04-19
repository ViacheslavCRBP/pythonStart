# 1. Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за четыре квартала для каждого предприятия.
# Программа должна определить среднюю прибыль
# (за год для всех предприятий) и отдельно вывести наименования предприятий,
# чья прибыль выше среднего и ниже среднего.

from collections import namedtuple

n = int(input('Введите количество фирм:  '))
print()

firma = namedtuple('firma', ['name', 'profit_1', 'profit_2', 'profit_3', 'profit_4', 'profit_year'])
firms = []
total = 0

for i in range(n):
    name = input(f'Фирма №{i+1} (название): ')
    profit_1 = float(input(f'Введите прибыль {i+1}-ой фирмы за 1 квартал:  '))
    profit_2 = float(input(f'Введите прибыль {i+1}-ой фирмы за 2 квартал:  '))
    profit_3 = float(input(f'Введите прибыль {i+1}-ой фирмы за 3 квартал:  '))
    profit_4 = float(input(f'Введите прибыль {i+1}-ой фирмы за 4 квартал:  '))
    profit_year = profit_1 + profit_2 + profit_3 + profit_4
    firms.append(firma(name=name, profit_1=profit_1, profit_2=profit_2, profit_3=profit_3, profit_4=profit_4, profit_year=profit_year))
    print()
    total += profit_year
print(f'Имеем список с данными о фирмах и их прибыли:\n{firms}')
print("*" * 50)

print(f'Фирмы без прибыли или с убытками: ')
for firma in firms:
    if firma.profit_year <= 0:
        print(firma.name)
print()

medium_total = round(total / n, 2)

print(f'Фирмы с прибылью, РАВНОЙ общей средней ({medium_total}): ')
for firma in firms:
    if firma.profit_year == medium_total:
        print(firma.name)
print()

print(f'Фирмы с прибылью МЕНЕЕ общей средней ({medium_total}): ')
for firma in firms:
    if firma.profit_year < medium_total:
        print(firma.name)
print()

print(f'Фирмы с прибылью БОЛЕЕ общей средней ({medium_total}): ')
for firma in firms:
    if firma.profit_year > medium_total:
        print(firma.name)
