"""
1. Подсчитать, сколько было выделено памяти под переменные
в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее
эффективным использованием памяти.
Примечание: По аналогии с эмпирической оценкой алгоритмов
идеальным решением будет:
a. выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
b. написать 3 варианта кода (один у вас уже есть);
проанализировать 3 варианта и выбрать оптимальный;

c. результаты анализа (количество занятой памяти в вашей среде
разработки) вставить в виде комментариев в файл с кодом.
Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
d. написать общий вывод: какой из трёх вариантов лучше и почему.
"""


import random
import sys

print('Версия ОС: ', sys.platform)
print('Версия Python: ', sys.version)
# Версия ОС:  win32
# Версия Python:  3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)]

a = 40
b = 40
min_elem = 0
max_elem = 10

print_matrix = False
show_det = True
details = False

matrix_1 = [[random.randint(min_elem, max_elem) for _ in range(b)] for _ in range(a)]

if print_matrix:
    for row in matrix_1:
        for el_1 in row:
            print(f'{el_1:>4}')
        print()


def trace_func(frame, event, arg):
    if event == "return":
        global us_memory
        for key in frame.f_locals.keys():
            size = show_size_obj(frame.f_locals[key])
            us_memory += size
            if show_det:
                print(f'{key} {type(frame.f_locals[key])}: {size}')
            if details:
                print()
    return trace_func


def show_size_obj(x, level=0):
    result_1 = sys.getsizeof(x)
    if details:
        if hasattr(x, '__iter__'):
            if hasattr(x, 'items'):
                for key, value in x.items():
                    result_1 += show_size_obj(key, level + 1)
                    result_1 += show_size_obj(value, level + 1)
            elif not isinstance(x, str):
                for item in x:
                    result_1 += show_size_obj(item, level + 1)
    return result_1
print('*' * 50)

def cache_optimized(matrix=None):
    if matrix is None:
        matrix = matrix_1
    min_array = [max_elem for _ in range(b)]
    for elem_2 in matrix:
        for i, el in enumerate(elem_2):
            if min_array[i] > el:
                min_array[i] = el
    min_el = min_elem - 1
    for i in min_array:
        if i > min_el:
            min_el = i
    return min_el
# Для функции cache_optimized суммарный объем памяти:
# 1268 bytes

def column_move(matrix=None):
    if matrix is None:
        matrix = matrix_1
    res = float('-inf')
    columns = len(matrix[0])
    rows = len(matrix)
    for col in range(columns):
        min_el = matrix[0][col]
        for elem_2 in range(rows):
            if min_el > matrix[elem_2][col]:
                min_el = matrix[elem_2][col]
        if res < min_el:
            res = min_el
    return res
# Для функции column_move суммарный объем памяти:
# 540 bytes

def with_transpose(matrix=None):
    if matrix is None:
        matrix = matrix_1
    res = float('-inf')
    tr_matrix = zip(*matrix)
    for tr_row in tr_matrix:
        min_el = tr_row[0]
        for el in tr_row:
            if el < min_el:
                min_el = el
        if res < min_el:
            res = min_el
    return res
# Для функции with_transpose суммарный объем памяти:
# 880 bytes

funcs = [(cache_optimized, ()), (column_move, ()), (with_transpose, ())]

sys.settrace(trace_func)
for func, args in funcs:
    us_memory = 0
    sys.call_tracing(func, args)
    print(f'Для функции {func.__name__} суммарный объем памяти:\n{us_memory} bytes')

''' 
Вывод: программа с наиболее эффективным использованием памяти - это with_transpose (вторая).
Потребление памяти в ней будет константным и предсказуемым за счет заранее определенных размеров переменных
(фиксированный размер массива). 
Более всего памяти требует первая программа.
Третья же является оптимальной - она простая по исполнению и не требует большого размера памяти.
'''

