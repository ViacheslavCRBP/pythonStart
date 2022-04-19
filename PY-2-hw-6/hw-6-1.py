'''1. Подсчитать, сколько было выделено памяти под переменные
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
d. написать общий вывод: какой из трёх вариантов лучше и почему. '''

# версия и разрядность ОС и интерпретатора Python:
# Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15)
# [MSC v.1929 64 bit (AMD64)] on win32

import sys

# функция, считающая размер исследуемых объектов:
def show_size_obj(x, level=0):
    print(f'for {x} {x.__class__} size:\n{sys.getsizeof(x)} bytes')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                show_size_obj(xx, level + 1)
        else:
            for xx in x:
                show_size_obj(xx, level + 1)
    print()
print('*' * 50)


print('Задача №3 урока 2:')
num = int(input('Введите натуральное число: '))
revers_ = 0
while num > 0:
    element = num % 10
    num = num // 10
    revers_ = revers_ * 10
    revers_ = revers_ + element

print(f'Число, обратное введенному, будет {revers_}')

show_size_obj(revers_)
# for 765 <class 'int'> size:
# 28 bytes
print('*' * 50)


print('Задача №5 урока 1:')
alphabet = 'abcdefghijklmnopqrstuvwxyz'

num_3 = int(input('Введите номер буквы в латинском алфавите (1- 26): '))
letter = alphabet[num_3 - 1]
print(f'Под номером {num_3} будет буква {letter}')

show_size_obj(num_3)
# for 12 <class 'int'> size:
# 28 bytes
print('*' * 50)


print('Задача №7 урока 1:')
year = num

if year % 4 == 0:
    if year % 400 == 0:
        print('Год високосный')
    elif year % 100 == 0:
        print('Год обычный')
    else:
        print('Год високосный')
else:
    print('Год обычный')

show_size_obj(year)
print('*' * 50)

print('Примеры расчета размера разных объектов')
show_size_obj(None)
show_size_obj(5**55)
show_size_obj([])
show_size_obj([5, 5.5, 55.55, 555.555, 5555555.555555])
show_size_obj({})

# Результаты расчета размера разных объектов (для примера):
# for None <class 'NoneType'> size:
# 16 bytes
#
# for 277555756156289135105907917022705078125 <class 'int'> size:
# 44 bytes
#
# for [] <class 'list'> size:
# 56 bytes
#
# for [5, 5.5, 55.55, 555.555, 5555555.555555] <class 'list'> size:
# 120 bytes
# for 5 <class 'int'> size:
# 28 bytes
#
# for 5.5 <class 'float'> size:
# 24 bytes
#
# for 55.55 <class 'float'> size:
# 24 bytes
#
# for 555.555 <class 'float'> size:
# 24 bytes
#
# for 5555555.555555 <class 'float'> size:
# 24 bytes
#
#
# for {} <class 'dict'> size:
# 64 bytes

'''Результаты анализа размера разных данных показывают, что переменные в формате int и float 
занимают минимальное значение памяти и имеют прямую зависимость лишь от величины переменной, 
в то время как словарь (даже пустой) занимает больше памяти.'''