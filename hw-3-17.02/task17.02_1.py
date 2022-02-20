# Задание 1:
# 1. Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление. Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль.

user_numbers = input('Введите два числа: ')
numbers = list(user_numbers.split())
num_1 = float(numbers[0])
num_2 = float(numbers[1])
if num_2 != 0:
    def my_division(num_1, num_2):
        return num_1 / num_2
    print(my_division(num_1, num_2))
else:
    print('На ноль делить нельзя')
