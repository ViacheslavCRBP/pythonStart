# Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60
# # (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Вызовите методы и покажите результат.

class Car:   # Реализуйте базовый класс Car.
    def __init__(self, speed, color, name, is_police=False):  # у класса должны быть следующие атрибуты:
        self.speed = speed                                      # speed, color, name, is_police (булево).
        self.color = color
        self.name = name
        self.polise = is_police
    def go(self):                               # А также методы: go, stop, turn(direction),
        print('Машина поехала.')                 # которые должны сообщать, что машина поехала,
    def stop(self):                             # остановилась, повернула (куда);
        print('Машина остановилась.')
    def turn(self, direction):
        print('Машина повернула', direction)
    def show_speed(self):                           # добавьте в базовый класс метод show_speed,
        print('Ваша скорость:', self.speed, 'км/ч')         #который должен показывать текущую скорость автомобиля;
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
class TownCar(Car):
    def show_speed(self):
        super().show_speed()                        # для классов TownCar и WorkCar переопределите метод show_speed.
        if self.speed > 60:                         # При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
            print('Превышение разрешенной скорости!')   #должно выводиться сообщение о превышении скорости.
class SportCar(Car):
    pass
class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Превышение разрешенной скорости!')
class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)
                                        # Создайте экземпляры классов, передайте значения атрибутов
town = TownCar(90, 'White', 'Town')
sport = SportCar(300, 'Red', 'Sport')
work = WorkCar(50, 'Orange', 'Work')
police = PoliceCar(120, 'Black', 'Police')
                                        # Выполните доступ к атрибутам, выведите результат.
                                        # Вызовите методы и покажите результат.
print()
print('TownCar:')
town.go()
town.show_speed()
town.stop()

print()
print('SportCar:')
sport.go()
sport.show_speed()
sport.turn('вправо')
sport.stop()

print()
print('WorkCar:')
work.go()
work.show_speed()
work.stop()

print()
print('PoliceCar:')
police.go()
police.turn('влево')
police.show_speed()
police.stop()
