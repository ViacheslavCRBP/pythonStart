# 2. Отсортируйте по возрастанию методом слияния одномерный
# вещественный массив, заданный случайными числами на
# промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

import random

# Создаем массив
n = int(input('Введите количество элементов массива:  '))
array = [random.randint(0, 50) for _ in range(n)]
print(array)
print('*' * 50)

def merge_sort(array, left_index, right_index):
    if left_index >= right_index:
        return

    middle = (left_index + right_index) // 2
    merge_sort(array, left_index, middle)
    merge_sort(array, middle + 1, right_index)
    merge(array, left_index, right_index, middle)

# Определяем функцию для объединения списка


def merge(array, left_index, right_index, middle):
# Создаем две части списка: левую и правую
    left_sublist = array[left_index:middle + 1]
    right_sublist = array[middle + 1:right_index + 1]

# Зададим начальные значения для переменных,
# которые мы используем для сохранения
# отслеживать, где мы находимся в каждом list1
    left_sublist_index = 0
    right_sublist_index = 0
    sorted_index = left_index

# проходим по обеим копиям, пока не закончятся элементы
    while left_sublist_index < len(left_sublist) and right_sublist_index < len(right_sublist):
# Если в левом списке есть меньший элемент, поместим его в отсортированную часть
        if left_sublist[left_sublist_index] <= right_sublist[right_sublist_index]:
            array[sorted_index] = left_sublist[left_sublist_index]
            left_sublist_index = left_sublist_index + 1
# В противном случае добавим элемент в правый список
        else:
            array[sorted_index] = right_sublist[right_sublist_index]
            right_sublist_index = right_sublist_index + 1
# продолжим двигаться по отсортированной части
        sorted_index = sorted_index + 1

# пройдемся по оставшимся элементам и добавим их
    while left_sublist_index < len(left_sublist):
        array[sorted_index] = left_sublist[left_sublist_index]
        left_sublist_index = left_sublist_index + 1
        sorted_index = sorted_index + 1

    while right_sublist_index < len(right_sublist):
        array[sorted_index] = right_sublist[right_sublist_index]
        right_sublist_index = right_sublist_index + 1
        sorted_index = sorted_index + 1

merge_sort(array, 0, len(array) - 1)
print(array)
