# Примеры использования модуля math
import math
r = 100  #Принимаем круг радиусом 100
print(2*r*math.pi) # ищем длину окружности
print((r**2)*math.pi) # ищем площадь круга
print((math.pow(r, 2))*math.pi)  # ищем площадь круга через встренную функцию pow
# определить расстояние между точками координат
x1=10
y1=10
x2=50
y2=100
l = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) # по теореме Пифагора, где sqrt - корень из числа
print(l)
# найти факториал 9
print(math.factorial(9))

# Примеры использования модуля random
# загадать случайное число от 0 до 100:
from random import randint, choice, sample, shuffle
print(randint(0, 100))
# Выбрать имя из списка:
players = ['Max', 'Leo', 'Kate', 'Ron', 'Bill']
print(choice(players))
# Выбрать Троих из списка:
print(sample(players, 3))
# перемешать карты в колоде
cards = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'T']
print(cards)
shuffle(cards)
print(cards)

# Сформировать случайный список из 10 чисел в диапазоне от 0 до 100
import random
my_list = [i for i in range(0, 100)]
print(random.sample(my_list, k=10))
