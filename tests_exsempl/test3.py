# Проверка пароля

while True:
    login = input('Введите логин >>> ') #логин (Hacker)
    pasword = input('Введите пароль >>> ') #пароль (12345)
    if pasword != '12345' or login != 'Hacker':
        print('Логин и пароль неверный!')
    else:
        print('Добро пожаловать, Хакер!')
        print()
        print('Вы успешно вошли в аккаунт')
        break