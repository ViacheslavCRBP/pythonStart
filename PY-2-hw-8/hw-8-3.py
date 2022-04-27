# 3. Написать программу, которая обходит не взвешенный
# ориентированный граф без петель, в котором все вершины
# связаны, по алгоритму поиска в глубину
# (Depth-First Search).
# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции,
# которая принимает на вход число вершин.


# исходный граф
N = int(input('\nКоличество вершин графа: '))

g = [[int(i >= j) for i in range(N)] for j in range(N)]
print(f'\nСоздаем граф: {g}\n')

def dijkstra(graph, start):
    length = len(graph)
    is_visited = [False] * length       # список длиной в leght - тут данные о том, посещали мы вершину или нет
    cost = [float('inf')] * length      # стоимость пути до конкретной вершины - изначально бесконечность 'inf'
    parent = [-1] * length              # данные о родителе изначально неизвестны, поэтому -1
    cost[start] = 0                     # стоимость первой вершины равна нулю - мы в ней уже находимся
    points_dict = {}                    # создаем пустой словарь
    min_cost = 0

    while min_cost < float('inf'):      # обходим граф в цикле
        is_visited[start] = True
        for i, vertex in enumerate(graph[start]):  # проходим по строке графа уровня start
            lst = []
            if vertex != 0 and not is_visited[i]:  # если у вершины есть ребро и данную вершину мы не посещали
                lst.append(start)
                points_dict[i] = lst
                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]  # в i вершине новое, более короткое расстояние
                    parent[i] = start               # указываем, какая вершина является родительской
                    lst.append(i)
                    points_dict[i] = lst
        min_cost = float('inf')                     # мин путь заменяем на бесконечность
        for i in range(length):                     # создаем цикл для проверки всех вершин графа
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i
    return cost, points_dict                        # вернуть из функции список путей для каждой вершины


s = int(input('От какой вершины идти: '))
print(dijkstra(g, s))

