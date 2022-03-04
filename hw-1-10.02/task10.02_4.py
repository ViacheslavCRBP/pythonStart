# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.


number = int(input('Введите целое положительное число '))
max_number = 0
while number > 0:
    if number % 10 > max_number:
        max_number = number % 10
        if max_number == 9:
            break
    else:
        number //= 10
print(f'Самая большая цифра в вашем числе: {max_number}')
#  print('Самая большая цифра в вашем числе:', max_number)



#  Рабочие варианты

#  в одну строку:
#  print('Самая большая цифра: ', sorted(input('Введите число: '), reverse=True)[0])

#   в одну строку:
#   print(max([int(num) for num in input('Введите число: ')]))

#  Рабочий вариант в две строки:
#  nums = input('Введите число: ')
#  print([idx for num in nums for idx in range(9, -1, -1) if str(idx) in nums][0])

#   Рабочий вариант в две строки:
#   print('Самая большая цифра: ', max(list(input('Введите число: '))))
#   print('Самая большая цифра: ', sorted(input('Введите число: '), reverse=True)[0])


