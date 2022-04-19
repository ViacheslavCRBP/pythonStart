# map
numbers = [1, 5 ,7, 3, 6, 8, 4]
# получить список квадратов:
# lambda x: x**2 - это будет функция
# numbers - это будет число
print(list(map(lambda x: x**2, numbers)))

# привести числа к строке
print(list(map(lambda x: str(x), numbers)))
