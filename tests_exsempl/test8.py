# Сортировка
numbers = [1, 5 ,7, 3, 6, 8, 4]
print(sorted(numbers))
print(sorted(numbers, reverse=True))

names = ['Max', 'Alex', 'Kate']
print(sorted(names))

cities = [('Тамбов', 1000), ('Воронеж', 1500), ('Саратов', 2000)]
print(sorted(cities))
def by_num(city):
    return city[1]
print(sorted(cities, key=by_num))


print(sorted(cities, key=lambda city: city[1]))