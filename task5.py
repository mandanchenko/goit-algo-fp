import uuid

import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="#9696F0"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

    def darken_color(self, n):
        # Ваша функція darken_color. Використовуйте значення n для чогось.
        r, g, b = int(self.color[1:3], 16), int(self.color[3:5], 16), int(self.color[5:7], 16)
        r, g, b = int(r - n), int(g - n), int(b - n)
        self.color = f'#{r:02X}{g:02X}{b:02X}'
        print(self.val, f'#{r:02X}{g:02X}{b:02X}')


def dfs_traversal_with_darken(node, n=1):
    if node is not None:
        # Виклик методу darken_color для поточного вузла
        node.darken_color(n)

        # Збільште значення n для наступного вузла
        n += 5

        # Виконайте обхід для лівого піддерева
        n = dfs_traversal_with_darken(node.left, n)

        # Виконайте обхід для правого піддерева
        n = dfs_traversal_with_darken(node.right, n)

    return n

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def dfs_traversal(node, n = 1):
    if node is not None:
        # Виконайте обхід для поточного вузла
        #print(node.val, end=' ')
        print(f"Node {node.val}, n = {n}")
        n += 1

        # Виконайте обхід для лівого піддерева
        n = dfs_traversal(node.left,n)


        # Виконайте обхід для правого піддерева
        n = dfs_traversal(node.right,n)

    return n


if __name__ == "__main__":
    # Створення дерева
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)

    # Відображення дерева
    #
    dfs_traversal(root)
    dfs_traversal_with_darken(root)
    draw_tree(root)