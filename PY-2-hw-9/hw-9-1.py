'''
Задача 1.
Определение количества различных подстрок с использованием хеш-функции.
Пусть на вход функции дана строка. Требуется вернуть количество различных
подстрок в этой строке.
Примечания:
* в сумму не включаем пустую строку и строку целиком;
* без использования функций для вычисления хэша (hash(), sha1()
или любой другой из модуля hashlib задача считается не решённой.
'''

import hashlib


def line_f(line: str):
    assert len(line) > 0, 'Строка не может быть пустой'

    length = len(line)
    sub_line = set()

    for i in range(length - 1):
        for j in range(i + 1, length + 1):
            g = hashlib.sha1(line[i:j].encode('utf-8')).hexdigest()
            sub_line.add(g)

    return len(sub_line)


my_line = input("Введите любую строку: ")

print(f'Строка имеет длину: {len(my_line)} elem')
print(f'Количество различных подстрок в строке: {line_f(my_line)}\nПримечание:\nв сумму подстрок не включены пустая строка и строка целиком')
