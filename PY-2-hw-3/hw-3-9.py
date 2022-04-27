# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
# Сначала считаем минимумы по столбцам, а потом среди них ищем мах.
# Без мин и мах!

import random
import numpy as np

side_x = int(input('Введите размер матрицы: '))
print('*' * 50)
side_y = side_x
matrix = [[random.randint(1, 100) for _ in range(side_x)] for _ in range(side_y)]
for line in matrix:
    for item in line:
        print(f'{item:>4}', end='')
    print()
print('*' * 50)

arr = np.array(matrix)
column = 0
i = 0
for column in arr:
    temp = arr[:, i]
    i += 1
    print(f'Cтолбец №{i}: {temp}')
print('*' * 50)

max_min_el = -1
for el in range(side_x):
    min_el = 100
    for i in range(side_y):
        if matrix[i][el] < min_el:
            min_el = matrix[i][el]
    print(f'Минимальный элемент в столбце №{el + 1}: {min_el}')
    if min_el > max_min_el:
        max_min_el = min_el
print('*' * 50)
print("Максимальный элемент среди списка минимальных: ", max_min_el)
