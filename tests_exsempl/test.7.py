# Календарь
date = '01.01.2014'
# переводим в строку через разделитель
d, m, y = date.split('.')
print(type)
print(d, m, y)
# создаем словари
days = {
    '01': 'первое',
    '02': 'второе'
}

months = {
    '01': 'января',
    '02': 'февраля'
}
result = f'{days[d]} {months[m]} {y} года'

print(result)
