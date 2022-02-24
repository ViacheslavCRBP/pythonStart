# Задание 3:
# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict.

print('Решение через <list>:')
number_month = int(input('Введите номер месяца (1-12): '))
seasons = ['Winter', 'Winter', 'Spring', 'Spring', 'Spring', 'Summer', 'Summer', 'Summer', 'Autumn', 'Autumn', 'Autumn',
           'Winter']
n = number_month - 1
if number_month >= 1 and number_month <= 12:
    print(number_month, '-th month of the year falls on', seasons[n])
else:
    print('', 'Внимательно прочитайте условие!', 'Ну и попробуйте заново...', sep='\n')

print()

print('Решение через <dict>:')
number_month = int(input('Введите номер месяца (1-12): '))
seasons = {1: 'Winter', 2: 'Winter', 3: 'Spring', 4: 'Spring', 5: 'Spring', 6: 'Summer', 7: 'Summer', 8: 'Summer',
           9: 'Autumn', 10: 'Autumn', 11: 'Autumn', 12: 'Winter'}
if number_month >= 1 and number_month <= 12:
    print(number_month, '-th month of the year falls on', seasons[number_month])
else:
    print('', 'Внимательно прочитайте условие!', 'Ну и попробуйте заново...', sep='\n')
