# Задание 2:
# Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().

# НЕ СДЕЛАНО

your_list = (input('Введите элементы списка: '))
my_list = list(your_list.split())
print('Список приведен в ', type(my_list))
print('Длина списка:', len(my_list), 'el')
print('Меняем местами пары элементов:')

part_list = my_list[0:2]
part_list.reverse()

for el in range(0, len(my_list), 2):
    print(list(part_list))

print()
i = 0
while i < len(my_list):
    part_list = my_list[i:]
    print(part_list)
    i += 1
