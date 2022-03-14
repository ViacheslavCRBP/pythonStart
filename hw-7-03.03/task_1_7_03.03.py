# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
#
# 31    32         3    5    32        3    5    8    3
# 37    43         2    4    6         8    3    7    1
# 51    86        -1   64   -8
#
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса
# Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
# складываем с первым элементом первой строки второй матрицы и т.д.

from random import randint

class Matrix:
    def __init__(self, nums):
        self.nums = nums

    def __str__(self):
        s = ''
        for i in range(len(self.nums)):
            for j in range(len(self.nums[i])):
                s += f'{self.nums[i][j]:03} '
            s += '\n'
        return s

    def __add__(self, other):
        nums = []
        for i in range(len(self.nums)):
            row = []
            for j in range(len(self.nums[i])):
                temp = self.nums[i][j] + other.nums[i][j]
                row.append(temp)
            nums.append(row)
        return Matrix(nums)

a = Matrix([[randint(0, 99) for _ in range(5)] for _ in range(5)])
b = Matrix([[randint(0, 99) for _ in range(5)] for _ in range(5)])
print(a)
print(b)
print('Матрица сумм:')
print(a + b)
