# 1. В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
# Примечание: нужно 8 разных ответов.

my_list = tuple(range(2, 100))
print('Список натуральных чисел в диапазоне от 2 до 99: ', my_list)

print('Вариант 1:')
multiple_list_2 = []
for el in my_list:
    if el % 2 == 0:
        multiple_list_2.append(el)
print(f'Числу 2 кратно {len(multiple_list_2)} чисел диапазона')

multiple_list_3 = []
for el in my_list:
    if el % 3 == 0:
        multiple_list_3.append(el)
print(f'Числу 3 кратно {len(multiple_list_3)} чисел диапазона')

multiple_list_4 = []
for el in my_list:
    if el % 4 == 0:
        multiple_list_4.append(el)
print(f'Числу 4 кратно {len(multiple_list_4)} чисел диапазона')

multiple_list_5 = []
for el in my_list:
    if el % 5 == 0:
        multiple_list_5.append(el)
print(f'Числу 5 кратно {len(multiple_list_5)} чисел диапазона')

multiple_list_6 = []
for el in my_list:
    if el % 6 == 0:
        multiple_list_6.append(el)
print(f'Числу 6 кратно {len(multiple_list_6)} чисел диапазона')

multiple_list_7 = []
for el in my_list:
    if el % 7 == 0:
        multiple_list_7.append(el)
print(f'Числу 7 кратно {len(multiple_list_7)} чисел диапазона')

multiple_list_8 = []
for el in my_list:
    if el % 8 == 0:
        multiple_list_8.append(el)
print(f'Числу 8 кратно {len(multiple_list_8)} чисел диапазона')

multiple_list_9 = []
for el in my_list:
    if el % 9 == 0:
        multiple_list_9.append(el)
print(f'Числу 9 кратно {len(multiple_list_9)} чисел диапазона')

print('*' * 33)
print('Вариант 2:')

multiple_list = [0] * 8
num_list = tuple(range(2, 10))
for el in my_list:
     for y in num_list:
         if el % y == 0:
             multiple_list[y - 2] += 1
el = 0
while el < len(multiple_list):
    print(f'Числу {el + 2} кратно {multiple_list[el]} чисел диапазона')
    el += 1

