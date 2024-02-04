import uuid
import heapq
import networkx as nx
import matplotlib.pyplot as plt


# Клас для представлення вузла бінарної купи
class HeapNode:
    def __init__(self, key, color="skyblue"):
        self.val = key
        self.color = color  # Додатковий атрибут для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла


# Функція для конвертації елементів купи в вузли
def convert_heap(heap):
    heap_nodes = [HeapNode(key=val) for val in heap]
    return heap_nodes


# Рекурсивна функція для додавання вузлів та ребер у граф для представлення бінарної купи
def add_heap_edges(graph, heap, pos, x=0, y=0, layer=1, index=0):
    if index < len(heap):
        node = heap[index]
        graph.add_node(node.id, color=node.color, label=node.val)
        if 2 * index + 1 < len(heap):
            left_child = heap[2 * index + 1]
            graph.add_edge(node.id, left_child.id)
            l = x - 1 / 2**layer
            pos[left_child.id] = (l, y - 1)
            add_heap_edges(
                graph, heap, pos, x=l, y=y - 1, layer=layer + 1, index=2 * index + 1
            )
        if 2 * index + 2 < len(heap):
            right_child = heap[2 * index + 2]
            graph.add_edge(node.id, right_child.id)
            r = x + 1 / 2**layer
            pos[right_child.id] = (r, y - 1)
            add_heap_edges(
                graph, heap, pos, x=r, y=y - 1, layer=layer + 1, index=2 * index + 2
            )


# Функція для візуалізації бінарної купи
def draw_heap(heap):
    heap_nodes = convert_heap(heap)
    heap_graph = nx.DiGraph()
    pos = {heap_nodes[0].id: (0, 0)}
    add_heap_edges(heap_graph, heap_nodes, pos)

    colors = [node[1]["color"] for node in heap_graph.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in heap_graph.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(
        heap_graph,
        pos=pos,
        labels=labels,
        arrows=False,
        node_size=2500,
        node_color=colors,
    )
    plt.show()


# Створення бінарної купи за допомогою heapq
heap = [4, 5, 10, 2, 7, 1]

# Відображення бінарної купи
draw_heap(heap)

# Створення бінарної купи з звичайного масиву
numbers = [5, 8, 4, 2, 9, 1, 7, 6, 3]
heapq.heapify(numbers)

# Відображення ще однієї бінарної купи
draw_heap(numbers)
