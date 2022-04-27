# Создание и удаление модулей
# Создайте модуль (модуль - программа на Python, т.е. файл с расширением .py).
# В нем создайте функцию создающую директории от dir_1 до dir_9 в папке из которой
# запущен данный код. Затем создайте вторую функцию удаляющую эти папки.

import os
def create_folders():
    for i in range(1, 10):
        folder_name = f'dir_{i}'
        os.mkdir(folder_name)
def delete_folders():
    for i in range(1, 10):
        folder_name = f'dir_{i}'
        os.rmdir(folder_name)
# при импортах функции из модуля происходит выполнение кода.
# Чтобы этого не было, надо добавить
# if __name__ == '__main__': и сдвинуть функции на tab
if __name__ == '__main__':
    create_folders()  # вызываем функцию или create_folders()
    delete_folders()  # или delete_folders()
