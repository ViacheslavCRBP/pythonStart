# Поиск наибольшей цифры в числе
nums = input('Введите число: ')
print([idx for num in nums for idx in range(9, -1, -1) if str(idx) in nums][0])