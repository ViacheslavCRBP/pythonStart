# Проверка делимости числа
#

a = int(input('Введите делимое: '))
b = int(input('Введите делитель: '))
c = a % b
if (c != 0):
    print(a, 'не делится на', b)
else:
    print(a, 'делится на', b)
