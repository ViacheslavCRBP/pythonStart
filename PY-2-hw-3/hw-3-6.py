# 6. В одномерном массиве найти сумму элементов,
# находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
# два варианта учесть: мах будет слева или справа?

import random
my_list = [random.randint(1, 20) for _ in range(10)]
print('Случайный массив: ', my_list)

max_el = max(list(filter(lambda el: el, [el for el in my_list])))
min_el = min(list(filter(lambda el: el, [el for el in my_list])))
max_ind = my_list.index(max_el)
min_ind = my_list.index(min_el)
print(f'Максимальный элемент массива ({max_el}) находится на позиции {max_ind + 1}.')
print(f'Минимальный элемент массива ({min_el}) находится на позиции {min_ind + 1}.')

# два варианта учесть: мах будет слева или справа?
if min_ind > max_ind:
    min_ind, max_ind = max_ind, min_ind

sum_el = 0
for el in range(min_ind + 1, max_ind):  # Сами минимальный и максимальный элементы в сумму не включать
    sum_el = sum_el + my_list[el]
print(f'Сумма элементов, находящихся между {min_ind + 1}-м и {max_ind + 1}-м элементами: {sum_el}.')
