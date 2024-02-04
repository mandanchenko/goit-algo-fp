import heapq


def print_table(distances, visited):
    # Верхній рядок таблиці
    print("{:<10} {:<10} {:<10}".format("Вершина", "Відстань", "Перевірено"))
    print("-" * 30)

    # Вивід даних для кожної вершини
    for vertex in distances:
        distance = distances[vertex]
        if distance == float("infinity"):
            distance = "∞"
        else:
            distance = str(distance)

        status = "Так" if vertex in visited else "Ні"
        print("{:<10} {:<10} {:<10}".format(vertex, distance, status))
    print("\n")


def dijkstra(graph, start):
    distances = {vertex: float("infinity") for vertex in graph}
    distances[start] = 0
    heap = [(0, start)]  # Мінімальна купа
    unvisited = list(graph.keys())
    visited = []

    while heap:
        current_distance, current_vertex = heapq.heappop(heap)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

        visited.append(current_vertex)
        unvisited.remove(current_vertex)

        # Вивід таблиці після кожного кроку
        print_table(distances, visited)

    return distances


# Приклад графа у вигляді словника
graph = {
    "A": {"B": 5, "C": 10},
    "B": {"A": 5, "D": 10, "C": 4},
    "C": {"A": 10, "B": 4, "D": 2},
    "D": {"B": 10, "C": 2, "E": 4},
    "E": {"D": 4},
}

# Виклик функції для вершини A
dijkstra(graph, "A")
