#  Массив размером 2m + 1, где m — натуральное число,
#  заполнен случайным образом. Найдите в массиве медиану.
#  Медианой называется элемент ряда, делящий его на две
#  равные части: в одной находятся элементы, которые
#  не меньше медианы, в другой — не больше медианы.
# Примечание: задачу можно решить без сортировки
# исходного массива.
# Но если это слишком сложно, используйте метод сортировки,
# который не рассматривался на уроках
# (сортировка слиянием также недопустима).

"""" Согдасно примечанию к задаче,
решение выполнил без сортировки исходного массива"""


import random

m = int(input('Введите натуральное число m: \n'))
# длина массива всегда будет нечетной

array = [random.randint(0, 100) for _ in range(2 * m + 1)]
print(f'Массив размером 2m + 1, где m — натуральное число {m}:\n{array}')
print('*' * 50)

mediana = array[len(array) // 2]
# mediana = array[m]
print(f'Медиана: {mediana} (с индексом {m})')

arr_down_2 = array[:m]
arr_up_2 = array[m + 1:]

print('*' * 50)
arr_up = []
print(f'\nЧасть массива, расположенная до медианы:', arr_down_2)
arr_down = []
print(f'Часть массива, расположенная после медианы:', arr_up_2)


def mediana_arr(array):
    for i in range(len(array)):
        if array[i] > mediana:
            arr_up.append(array[i])
        elif array[i] < mediana:
            arr_down.append(array[i])


mediana_arr(array)
print(f'\nЧасть массива, значения элементов которой МЕНЬШЕ значения медианы:\n{arr_down}')
print(f'Часть массива, значения элементов которой БОЛЬШЕ значения медианы:\n{arr_up} ')
