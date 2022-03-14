# Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу
# декоратора @property.

from abc import ABC, abstractmethod


# Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
class Clothes(ABC):
    @abstractmethod
    def rate(self):
        pass


# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    # Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5)
    @property
    def rate(self):
        return self.v // 6.5 + 0.5


# Реализовать общий подсчет расхода ткани на пальто.
def sum_rate_coat(list_coats):
    dress = 0
    for suit in list_coats:
        dress += suit.rate
    return dress


class Costume(Clothes):
    def __init__(self, h):
        self.h = h

    # Для определения расхода ткани по каждому типу одежды использовать формулы: для костюма (2*H + 0.3).
    @property
    def rate(self):
        return 2 * self.h + 0.3


# Реализовать общий подсчет расхода ткани на костюмы.
def sum_rate_costume(list_costume):
    outfit = 0
    for costume in list_costume:
        outfit += costume.rate
    return outfit


# Данные для проверки работы этих методов:
coat_1 = Coat(38)
coat_2 = Coat(42)
coat_3 = Coat(50)
coat_4 = Coat(54)
coat_5 = Coat(60)
list_suits = [coat_1, coat_2, coat_3, coat_4, coat_5]

costume_1 = Costume(1.80)
costume_2 = Costume(1.88)
costume_3 = Costume(1.76)
costume_4 = Costume(1.58)
costume_5 = Costume(1.98)
list_costumes = [costume_1, costume_2, costume_3, costume_4, costume_5]

print(coat_1.rate)
print(coat_2.rate)
print(coat_3.rate)
print(coat_4.rate)
print(coat_5.rate)
print('Всего ткани на 5 пальто:', sum_rate_coat(list_suits), 'm')

print()
print(costume_1.rate)
print(costume_2.rate)
print(costume_3.rate)
print(costume_4.rate)
print(costume_5.rate)
print('Всего ткани на 5 костюмов:', sum_rate_costume(list_costumes), 'm')
