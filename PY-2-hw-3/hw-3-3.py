# 3. В массиве случайных целых чисел поменять местами
# минимальный и максимальный элементы.
# (без функций min /  max)

import random
long = int(input('Введите количество элементов массива: '))
my_list = [random.randint(0, 100) for _ in range(long)]
print('Случайный массив: ', my_list)

index_min = 0
index_max = 0
for el in range(1, long):
    if my_list[el] > my_list[index_max]:
        index_max = el
    elif my_list[el] < my_list[index_min]:
        index_min = el
print(f'Минимальный элемент массива: {(my_list[index_min])}')
print(f'Максимальный элемент массива: {(my_list[index_max])}')

my_list[index_min], my_list[index_max] = my_list[index_max], my_list[index_min]
print(f'Максимальный и минимальный элемент массива поменялись местами: {my_list}')

