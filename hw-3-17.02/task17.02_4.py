# Задание 4:
# Программа принимает
# действительное положительное число x и целое отрицательное число y.
# Выполните возведение числа x в степень y.
# Задание реализуйте в виде функции my_func(x, y).
# При решении задания нужно обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **,
# предусматривающая использование цикла.


# Программа принимает действительное положительное число x
# и целое отрицательное число y в пределах диапазона, заданного пользователем:
import random
n = int(input('Введите максимальное значение для границ диапазона чисел (X,Y): '))
x = float(random.randint(1, n))
y = - (random.randint(1, n))
print('Программа выбрала следующие значения:', 'X =', x, ';  Y =', y)

# создаем функцию для расчета с помощью оператора ** (Вариант 1):
def degree_func(n_1, n_2):
    return n_1 ** n_2
print('X**Y =', degree_func(x, y))


# создаем функцию для расчета через цикл (Вариант 2):
# могу понять, почему она не считает?
def degree_func(n_1, n_2):
    i = 1
    while i <= n_2:
        return 1 / n_1
        i += 1
        if i > n_2:
            break
print('X**Y =', degree_func(x, y))
