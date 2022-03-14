import sys, os

for arg in sys.argv:
    print(arg)
    print(type(arg))

def ping():  # параметр ping - функция выводит pong
    print('pong')
ping()

def hello(name):  #  функция приветствия пользователя
    print('Hello', name)
hello('Leo')

def get_info():  # через параметр list показать содержимое текущей директории (папки)
    print(os.listdir())
get_info()

