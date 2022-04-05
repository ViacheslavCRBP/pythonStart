# Создание своего модуля
import os, sys

print(os.name)   # имя ОС (если windoos 10  -  покажет nt)
print(os.getcwd())      # текущая рабочая директория
new_path = os.path.join(os.getcwd(), 'new_f')     # Создаем новый путь
os.mkdir(new_path)     # создаем папку по новому пути
print(sys.executable) # путь до интерпретатора - python.exe
print(sys.platform)  # информация о платформе - win32

# В папке с модулем надо создать 5 подпапокб названия которых состоят из платформы,
# на которой запущен интерпретатор (у мнея это win32), начиная с номера 1: win32_1, win32_2 ...

# import os, sys - делаем, если не сделано выше!
name = sys.platform  # информация о платформе - win32
for i in range(1, 6):
    new_path = os.path.join(os.getcwd(), '{}_{}'.format(name, i)) # создаем переменную (new_path),
    # которую соберем из двух частей: 1) это путь до модуля - os.getcwd(), 2) это название платформы и номер (name, i)
    os.mkdir(new_path)  # создаем новую папку и передаем туда созданный путь
# так у нас должно создаться от 1 до 5 папок
sys.exit()  # выход из python
print('не выполнится после sys.exit() т.е. после выхода из python')
