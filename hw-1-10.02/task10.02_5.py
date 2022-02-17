#  5
#  Запросите у пользователя значения выручки и издержек фирмы.
#  Определите, с каким финансовым результатом работает фирма.
#  Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки.
#  Выведите соответствующее сообщение.
#
#  6
#  Если фирма отработала с прибылью, вычислите рентабельность выручки.
#  Это отношение прибыли к выручке. Далее запросите численность сотрудников фирмы и
#  определите прибыль фирмы в расчёте на одного сотрудника.

#  Примечание: в данном решении сведены две задачи (5 и 6) в один алгоритм.

debet = int(input('Введите значение выручки фирмы: '))
credit = int(input('Введите значение издержек фирмы: '))
ballans = debet - credit
if ballans > 0:
    print('В результате работы фирмы получена прибыль в размере:', ballans, 'руб')
    print('Рентабельность составила:', ballans * 100 // debet, '%')
    workers = int(input('Введите количество сотрудников фирмы: '))
    print('Прибыль фирмы в расчёте на одного сотрудника составила', ballans // workers, 'руб')
elif ballans < 0:
    print('В результате работы фирмы имеются убытки в размере:', ballans, 'руб')
else:
    print('Результат работы фирмы нулевой. У налоговой будут вопросы к фирме.')
