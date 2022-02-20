# Задание 2:
# Выполнить функцию, которая принимает несколько параметров,
# описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.

name = input('Введите имя: ')
surname = input('Введите фамилию: ')
year = input('Введите год рождения: ')
city = input('Введите город проживания: ')
email = input('Введите е-майл: ')
phone = input('Введите номер телефона: ')
# Variant 1 - именованные параметры
print()
def user_data_1(data_1, data_2, data_3, data_4, data_5, data_6):
    print(f'{data_1} {data_2}: {data_3} года, г.{data_4}, e-mail:{data_5}; тел:{data_6}')
user_data_1(data_1=name, data_2=surname, data_3=year, data_4=city, data_5=email, data_6=phone)


# Другие варианты пказались более простыми и интересными:
# Variant 2 - позиционные параметры
print()
def user_data_2():
    print(name, surname, ':', year, city, email, phone)
user_data_2()

# Variant 3 - неопределённое число позиционных параметров
print()
def user_data_3(*data):
    return data
print(user_data_3(name, surname, year, city, email, phone))
