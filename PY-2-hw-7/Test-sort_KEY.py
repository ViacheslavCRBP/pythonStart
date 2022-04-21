# Алгоритм сортировки с использованием ключа

# создадим именованный кортеж:

from collections import namedtuple
from operator import attrgetter

Person = namedtuple('Person', 'name, age')

p_1 = Person('Vasya', 25)
p_2 = Person('Kolya', 30)
p_3 = Person('Oya', 23)

people = [p_1, p_2, p_3]
print(people)

# Сортируем по имени по алфавиту через sorted:
result = sorted(people)
print(result)

# Сортируем по возрасту через sorted, нужна функция
# чтобы  возвращать возраст персонажа, и она будет ключом:
def by_age(person):
    return person.age
# Можно использовать встроенную функцию: from operator import attrgetter -
# attrgetter - позволяет сортировать словарь по любому атрибуту

result = sorted(people, key=by_age)
print(result)

# можно импортировать attrgetter из модуля operator:
# from operator import attrgetter
result_2 = sorted(people, key=attrgetter('age'))
print(result_2)

