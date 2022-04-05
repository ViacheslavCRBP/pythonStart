# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2 ...
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

# создаем словарь для перевода:
words = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре', 'Five': 'Пять'}

with open('task_4_5.txt', 'r') as numbers, open('rus_task_4_5.txt', 'w', encoding='utf-8') as rus_numbers:
    numbers_line = numbers.readlines()
    for line in numbers_line:
        text = line.split()
        rus_words = words.get(text[0])
        rus_numbers.write(f'{line.replace(text[0], rus_words)}')
        print('\n')
