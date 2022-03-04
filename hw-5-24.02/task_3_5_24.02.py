# Создать текстовый файл (не программно). Построчно записать фамилии сотрудников
# и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч,
# вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

with open('task_3_5.txt', 'r', encoding='utf-8') as salary:
    content = salary.readlines()
print(content)
print(type(content))
wokers = {}
sum_salary = 0
for line in content:
    work_line = line.split()
    wokers.update({work_line[0]: float(work_line[1])})
    sum_salary += float(work_line[1])
medium_sal = sum_salary // len(wokers)
print('Средний доход на всех сотрудников: ', medium_sal)
for name, cash in wokers.items():
    if cash < 20000:
        print(f'Сотрудники с окладом менее 20.000 руб.: {name} ({cash} руб.)')
