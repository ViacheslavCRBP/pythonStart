'''
Задача 2.
Закодируйте любую строку по алгоритму Хаффмана.
'''

from collections import Counter
import random
from binarytree import build

long = int(input('Введите количество элементов массива: '))
my_list = [random.randint(1, 5) for _ in range(long)]
print('Случайный массив: ', my_list)

numbers = Counter(my_list)
print(numbers)

s = build(numbers)
print(s)

#   не успел доделать
