graph = {
    (1, 2): 10,
    (2, 1): 10,
    (1, 3): 15,
    (3, 1): 15,
    (1, 4): 20,
    (4, 1): 20,
    (2, 4): 25,
    (4, 2): 25,
    (2, 3): 35,
    (3, 2): 35,
    (3, 4): 30,
    (4, 3): 30,
}

vertices = [1, 2, 3, 4]  # список всех вершин
start_vertex = 3  # фиксированная стартовая вершина


# Функция для вычисления длины пути
def calculate_path_length(path):
    length = 0
    for i in range(len(path) - 1):
        length += graph.get((path[i], path[i + 1]), float("inf"))
    return length


# Рекурсивная функция для поиска всех маршрутов
def find_paths(visited, current_path):
    # Если все вершины посещены, возвращаемся в начальную вершину
    if len(visited) == len(vertices):
        current_path.append(start_vertex)
        return [current_path[:]]  # Вернули копию пути как список из одного элемента

    paths = []
    for vertex in vertices:
        if vertex not in visited:
            visited.add(vertex)
            current_path.append(vertex)

            # Рекурсивно ищем все маршруты из этой вершины
            paths.extend(find_paths(visited, current_path))

            # Откатываем изменения для других путей
            visited.remove(vertex)
            current_path.pop()

    return paths


# Ищем все возможные маршруты, которые начинаются и заканчиваются в start_vertex
visited = {start_vertex}
paths = find_paths(visited, [start_vertex])

# Поиск маршрута с минимальной длиной
min_path = None
min_length = float("inf")

for path in paths:
    current_length = calculate_path_length(path)
    if current_length < min_length:
        min_length = current_length
        min_path = path

# Выводим результат
print(f"Оптимальный маршрут: {min_path}")
print(f"Минимальная длина пути: {min_length}")
