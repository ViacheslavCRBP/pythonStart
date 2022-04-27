# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться
# Нужно проверить и второй от минимального элемент.

import random
long = int(input('Введите количество элементов массива: '))
my_list = [random.randint(0, 10) for _ in range(long)]
print('Случайный массив: ', my_list)

index_min_1 = 0
index_min_2 = 0

for el in range(1, long):
    if my_list[el] < my_list[index_min_1]:
        index_min_1 = el
print(f'Минимальный элемент массива: {my_list[index_min_1]}')

y = my_list[index_min_1]
my_list.pop(index_min_1)
for el in range(1, long - 1):
    if my_list[el] < my_list[index_min_2]:
        index_min_2 = el
print(f'Второй минимальный элемент массива: {my_list[index_min_2]}')
if y == my_list[index_min_2]:
    print('В данном массиве два минимальных элемента между собой равны (оба минимальны).')
