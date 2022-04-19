# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный»
# и «максимальный отрицательный». Это два абсолютно разных значения.

import random
my_list = [random.randint(-100, 100) for _ in range(20)]
print('Список случайных чисел: ', my_list)

# Вариант 1
max_negative = max(list(filter(lambda el: el < 0, [el for el in my_list])))
ind = my_list.index(max_negative)
print(f'Вариант 1: Максимальный отрицательный элемент массива ({max_negative}) находится на позиции {ind + 1}.')

# Вариант 2
max_neg = -1
indx = 0
while indx < 20:
    if my_list[indx] < 0 and max_neg == -1:
        max_neg = indx
    elif my_list[indx] < 0 and my_list[indx] > my_list[max_neg]:
        max_neg = indx
    indx += 1
print(f'Вариант 2: Максимальный отрицательный элемент массива ({my_list[max_neg]}) находится на позиции {max_neg + 1}.')

