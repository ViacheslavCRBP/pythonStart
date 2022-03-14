# Фильтрация

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 13)
# получим только четные числа
def is_even(number):
    return number % 2 == 0
result = filter(is_even, numbers)
result = list(result)
print(result)

# ПОлучить строки длиннее 3-х символов
names = ['Max', 'Alex', 'Kate', 'Dog', 'Bill']
print(list(filter(lambda x: len(x)>3, names)))