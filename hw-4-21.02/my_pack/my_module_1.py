def payroll(firs_name, time_work, wage_rate, pers_premium):
    payment = time_work * wage_rate + pers_premium
    print('Сотрудник: ', firs_name)
    print(f'Заработная плата составит {payment} рублей.')
if __name__ == '__main__':
    payroll('Петров П.П.', 30, 550, 3330)
