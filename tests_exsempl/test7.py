# Комп угадывает число

import random
min_num = 1
max_num = 100
result = None
while result != "=":
    num = random.randint(min_num, max_num)
    print(num)
    result = input('поставьте знак: больше или меньше загаданного числа?) = > <  ')
    if result == ">":
        min_num = num +1
    elif result == "<":
        max_num = num - 1
print('Число угадано')
