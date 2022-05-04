# 4. Определить, какое число в массиве встречается чаще всего.
# * диапазон значений меньше размера массива!

import random
long = int(input('Введите количество элементов массива: '))
my_list = [random.randint(1, 10) for _ in range(long)]
print('Случайный массив: ', my_list)

my_set = set(my_list)
print('Множество уникальных чисел: ', my_set)

oft_el = None   # наиболее часто встречаемое значение
nums_el = 0     # сколько oft_el

for el in my_set:
    nums = my_list.count(el)
    if nums > nums_el:
        nums_el = nums
        oft_el = el
    elif nums == nums_el:
        print(f'В массиве несколько чисел встречаются одинаково часто.')
print(f'Чаще всего встречается число {oft_el}.')