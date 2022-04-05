# УРОК 3.
# Задание 3:
# Реализовать функцию my_func(),
# которая принимает три позиционных аргумента
# и возвращает сумму наибольших двух аргументов.

numbers = []
for i in range(3):
    number = int(input('Введите число: '))
    numbers.append(number)
result = (sorted(numbers))
result.reverse()
print('Список по убыванию: ', result)
# создаем функцию для расчета
def sum_func(n_1, n_2, n_3):
    return n_1 + n_2 + n_3 - n_3
print('Сумма двух наибольших аргументов: ', sum_func(result[0], result[1], result[2]))

