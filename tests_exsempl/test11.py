# Использование функций при расчете урона игрокам:
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health = 100,
# damage = 50.
# Поэкспериментируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2).
# Примечание: имена аргументов можете указать свои. #
# ## Функция в качестве аргумента будет принимать атакующего и атакуемого.
# В теле функция должна получить параметр damage атакующего и отнять это количество от health атакуемого.
# Функция должна сама работать со словарями и изменять их значения.
# Давайте усложним предыдущее задание.
# Измените сущности, добавив новый параметр - armor = 1.2 (величина брони персонажа)
# Теперь надо добавить новую функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно, у вас должно быть 2 функции:
# Наносит урон. Это улучшенная версия функции из задачи 3.
# Вычисляет урон по отношению к броне.
# Примечание. Функция номер 2 используется внутри функции номер 1 для вычисления урона и вычитания его из здоровья персонажа.

player_name = input('Введите имя игрока ')
player = {
    'name': player_name,
    'health': 300,
    'damage': 80,
    'armor': 1.2
}
eneme_name = input('Введите имя врага ')
eneme = {
    'name': eneme_name,
    'health': 70,
    'damage': 150,
    'armor': 1.5
}
def get_damage(damage, armor):
    return damage / armor

def attack(unit, target):
    damage = get_damage(unit['damage'], target['armor'])
    target['health'] -= damage

attack(player, eneme)
print(eneme)

attack(eneme, player)
print(player)