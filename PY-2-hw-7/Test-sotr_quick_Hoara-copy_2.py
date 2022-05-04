#  Сортировка Быстрая ХОАРА  (QUICK):
#  БЕЗ ИСПОЛЬЗОВАНИЯ ДОП.ПАМЯТИ!!
import random

size = 10
array = [i for i in range(size)]
random.shuffle(array)  # метод shuffle() перемешал значения в array
print(array)
print('*' * 50)

def quick_sort_no_memory(array, first, last):

    if first >= last:
        return
    print(array)  #  смотрим промежуточные значения

    pivot = array[random.randint(first, last)]
    i, j = first, last  # нужны, чтобы отслеживать индекс
    # позволят менять местами вокруг опорного (pivot)
    while i <= j:
        while array[i] < pivot:
            i += 1
        while array[j] > pivot:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i, j = i + 1, j - 1

    quick_sort_no_memory(array, first, j)
    quick_sort_no_memory(array, i, last)

#  просим функцию отсортировать весь массив
#  от начала до конца:
quick_sort_no_memory(array, 0, len(array) - 1)
print(array)
