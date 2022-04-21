#  Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров.

class Worker: #  Реализовать базовый класс Worker (работник).
    def __init__(self, name, surname, position, wage, bonus):  # определить атрибуты: name, surname, position
        # (должность), income (доход);
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}  # последний атрибут должен быть защищённым
        # и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};

class Position(Worker): # создать класс Position (должность) на базе класса Worker;
    def get_full_name(self): # в классе Position реализовать методы получения
        # полного имени сотрудника (get_full_name)
        return '{0} {1}'.format(self.name, self.surname)
    def get_total_income(self): # и дохода с учётом премии (get_total_income);
        return self._income['wage'] + self._income['bonus']
employee = Position('Петр', 'Смирнов', 'Менеджер', 50000, 10000) # проверить работу примера на реальных данных: создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров.
print(f'Имя: {employee.name}', f'Фамилия: {employee.surname}', f'Должность: {employee.position}',
      f'Оклад и премия работника: {employee._income.values()}', '-'*50, sep='\n')
print(f'Для работника {employee.get_full_name()} к выдаче: {employee.get_total_income()} руб.')
