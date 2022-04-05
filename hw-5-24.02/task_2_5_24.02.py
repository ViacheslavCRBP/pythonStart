# Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.

# Создаем вручную файл task_2_5.txt

with open('task_2_5.txt', 'r') as lorem:
    print('Список строк (через разделитель): \n', lorem.readlines())
print()
with open('task_2_5.txt', 'r') as lorem:
    сount = sum(1 for line in lorem)
    print('Количество строк:', сount)
print()
with open('task_2_5.txt', 'r') as lorem:
    for line in lorem:
        print(line.replace('\n', ''))
        result = len(line.split())
        print("- в этой строке", str(result), "слов.")
        print()
