# Выбор одинаковых элементов из двух списков

fruits1 = ['banana', 'appele', 'orange', 'kiwi', 'pear']
fruits2 = ['melon', 'kiwi', 'onion', 'pear', 'berry']
# Var 1
result1 = []
for fruit in fruits1:
    if fruit in fruits2:
        result1.append(fruit)
print(result1)

# Var 2
result2 = []
result2 = [fruit for fruit in fruits1 if fruit in fruits2]
print(result2)

# Выбор НЕодинаковых элементов из двух списков:
# Var 1
result3 = []
for fruit in fruits1:
    if fruit in fruits2:
        pass
    else:
        result3.append(fruit)
for fruit in fruits2:
    if fruit in fruits1:
        pass
    else:
        result3.append(fruit)
print(result3)

# Var 2
result4 = []
result4 = [fruit for fruit in fruits1 if not fruit in fruits2] + [fruit for fruit in fruits2 if not fruit in fruits1]
print(result4)

