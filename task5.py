import uuid

import networkx as nx
import matplotlib.pyplot as plt

from collections import deque


class Node:
    def __init__(self, key, color="#3C3C60"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

    def change_color(self, n):
        r, g, b = (
            int(self.color[1:3], 16),
            int(self.color[3:5], 16),
            int(self.color[5:7], 16),
        )
        r, g, b = min(int(r + n), 255), min(int(g + n), 255), min(int(b + n), 255)
        self.color = f"#{r:02X}{g:02X}{b:02X}"
        print(self.val, self.color)


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(
            node.id, color=node.color, label=node.val
        )  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {
        node[0]: node[1]["label"] for node in tree.nodes(data=True)
    }  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(
        tree,
        pos=pos,
        labels=labels,
        arrows=False,
        node_size=2500,
        node_color=colors,
        font_color="#ebba34",
    )
    plt.show()


# Повернення всім нодам дефолтного коліру
def set_all_nodes_color(root, color="#3C3C60"):
    if root is not None:
        # Встановлення коліру для поточного вузла
        root.color = color

        # Рекурсивний виклик для лівого піддерева
        set_all_nodes_color(root.left, color)

        # Рекурсивний виклик для правого піддерева
        set_all_nodes_color(root.right, color)


# Функція, яка змінює колір згідно обходу в ширину
def bfs_traversal_with_color(root, step=10):
    if root is None:
        return

    # Ініціалізація черги та початкового значення n
    queue = deque([root])
    n = 1

    while queue:
        # Отримання та видалення першого елемента з черги
        current_node = queue.popleft()

        # Виклик методу darken_color для поточного вузла
        current_node.change_color(n)

        # Збільште значення n для наступного вузла
        n += step

        # Додавання дітей поточного вузла до черги (якщо вони існують)
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)


# Функція, яка змінює колір згідно обходу в глибину
def dfs_traversal_with_color(node, step=10, n=1):
    if node is not None:
        # Виклик методу darken_color для поточного вузла
        node.change_color(n)

        # Збільште значення n для наступного вузла
        n += step

        # Виконайте обхід для лівого піддерева
        n = dfs_traversal_with_color(node.left, step, n)

        # Виконайте обхід для правого піддерева
        n = dfs_traversal_with_color(node.right, step, n)

    return n


if __name__ == "__main__":
    # Створення дерева
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)

    # Робимо обход в ширину
    bfs_traversal_with_color(root, 12)
    # Малюємо дерево
    draw_tree(root)
    # Повертаємо дефолтні значення
    set_all_nodes_color(root)
    # Робимо обход в глибину
    dfs_traversal_with_color(root, 15)
    # Малюємо дерево
    draw_tree(root)
