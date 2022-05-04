'''
2. Доработать алгоритм Дейкстры (рассматривался на уроке),
 чтобы он дополнительно возвращал список вершин,
 которые необходимо обойти.
'''
#
from collections import deque

# исходный граф
g = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0],
]


def dijkstra(graph, start):
    lenght = len(graph)
    is_visited = [False] * lenght  # список длиной в leght - тут данные о том, посещали мы вершину или нет
    cost = [float('inf')] * lenght  # стоимость пути до конкретной вершины - изначально бесконечность 'inf'
    parent = [-1] * lenght  # данные о родителе изначально неизвестны, поэтому -1
    cost[start] = 0  # стоимость первой вершины равна нулю - мы в ней уже находимся
    min_cost = 0

    parent_start = start  # добавляем первого родителя
    parent_2 = [None] * lenght  #  указываем на отсутствие родителей по всем путям

    while min_cost < float('inf'):
        is_visited[start] = True

        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:  # если у вершины есть ребро и данную вершину мы не посещали
                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]  # записываем более короткое расстояние
                    parent[i] = start  # указываем, какая вершина является родительской
        #  в этом цикле мы проверили все смежные вершины и записали минимальные расстояния до каждой

        min_cost = float('inf')  # минимальный путь заменяем на бесконечность
        for i in range(lenght):  # создаем цикл для проверки всех вершин графа
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i

    for el in range(lenght):
        if el != parent_start:
            num = el
            if parent[num] != -1:
                parent_2[el] = deque([num])
                while True:
                    parent_2[el].appendleft(parent[num])
                    if parent[num] == parent_start:
                        break
                    num = parent[num]
            else:
                parent_2[el] = [f'Нет вариантов']

    return cost, parent_2  # вернуть из функции список путей для каждой вершины
    # и список вершин,которые необходимо обойти

s = int(input('От какой вершины идти: '))
print(dijkstra(g, s))

cost, parent_2 = dijkstra(g, s)

for i in range(len(g)):
    if i != s:
        print(f'Кратчайший путь до вершины {i}:'
              f' {list(parent_2[i])}\nстоимость: {cost[i]} у.е.')
