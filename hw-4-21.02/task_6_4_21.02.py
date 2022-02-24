# УРОК 4
# Задача 6
# Реализовать два небольших скрипта:
# итератор, генерирующий целые числа, начиная с указанного;
# итератор, повторяющий элементы некоторого списка, определённого заранее.
# Подсказка: используйте функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Предусмотрите условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3. При достижении числа 10 — завершаем цикл.
# Вторым пунктом необходимо предусмотреть условие, при котором повторение элементов списка прекратится.

import random
from itertools import count, cycle

n_1 = int(input('Число, с которого начать генерацию: '))
n_2 = int(input('Число, на котором закончить генерацию: '))
my_list = [i for i in range(n_1, n_2+1)]
print()

# Вариант №1:
print('Список, из которого выбирается случайное число: ', my_list)
num_1 = random.choice(my_list)
print('Случайное число по Варианту №1: ', num_1)
print()

# Вариант №2:
print('Случайные числа по Варианту №2: ')
for el_count in count(n_1):
    if el_count == n_2:
        break
    else:
        print(random.choice(my_list))
print()

# Вариант №3:
el_cycle = cycle(my_list)
print('Случайные числа по Варианту №3: ')
print(next(el_cycle))
print(next(el_cycle))
print(next(el_cycle))
print(next(el_cycle))
print(next(el_cycle))
print(next(el_cycle))
print(next(el_cycle))
print()

# Вариант №4:
print('Случайные числа по Варианту №4: ')
num_2 = 0
for elem_cycle in cycle(my_list):
    if num_2 > n_2:
        break
    print(elem_cycle)
    num_2 += 1
