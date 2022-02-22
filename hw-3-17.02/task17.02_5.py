# Задание 5:
# Программа запрашивает у пользователя строку чисел,
# разделённых пробелом. При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
# Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму
# этих чисел к полученной ранее сумме и после этого завершить программу.

def sum_numbers(numbers, stop):
    my_sum = 0
    for i in numbers:
        if i == stop:
            print('Введена команда СТОП')
            break
        my_sum += int(i)
    return my_sum
stop_sum = '/'
end = False
sum_el = 0
while not end:
    user_numbers = input('Введите несколько чисел: ').split()
    numbers = list(user_numbers)
    sum_el += sum_numbers(numbers, stop_sum)
    end = stop_sum in numbers
    print(f'Сумма текущая = {sum_el}')
print('Программа завершена:', end, f'. Финальная сумма >>> {sum_el}')
