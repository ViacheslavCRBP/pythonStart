# 8. Матрица 5x4 заполняется вводом с клавиатуры,
# кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки
# и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу
# Сумму лучше считать при формировании матрицы.

X = 5
Y = 4
matrix = []
for el in range(X):
    line = []
    summa = 0
    print(f'Введите {Y} элемента {el + 1}-ой строки: ')
    for i in range(X-1):
        elem = int(input())
        summa += elem
        line.append(elem)
    line.append(summa)
    matrix.append(line)
    matrix.append('-' * 5)
print('*' * 25)
for el in matrix:
    for item in el:
        print(f'{item:>4}', end='')
    print()
