"""
Завдання 1. Структури даних. Сортування. Робота з однозв'язним списком

Для реалізації однозв'язного списку (приклад реалізації можна взяти з конспекту) необхідно:

написати функцію, яка реалізує реверсування однозв'язного списку, змінюючи посилання між вузлами;
розробити алгоритм сортування для однозв'язного списку, наприклад, сортування вставками або злиттям;
написати функцію, що об'єднує два відсортовані однозв'язні списки в один відсортований список.
"""


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    # пункт 1 - реверсування списку
    def reverse_list(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # пункт 2 - сортування вставками однозв'язного списку
    def insertion_sort(self):
        if self.head is None or self.head.next is None:
            return

        sorted_head = None  # Початок відсортованого списку

        current = self.head
        while current:
            next_node = current.next

            # Вставка поточного вузла в відсортований список
            sorted_head = self._insert_in_sorted(sorted_head, current)

            current = next_node

        self.head = sorted_head

    def _insert_in_sorted(self, sorted_head, new_node):
        if sorted_head is None or sorted_head.data >= new_node.data:
            new_node.next = sorted_head
            sorted_head = new_node
        else:
            current = sorted_head
            while current.next and current.next.data < new_node.data:
                current = current.next
            new_node.next = current.next
            current.next = new_node

        return sorted_head


# пункт 3 - об'єднання 2х відсортованих списків в один відсортований список.
def merge_sorted_lists(list1, list2):
    merged_list = LinkedList()
    merged_head = Node()
    merged_current = merged_head

    current1 = list1.head
    current2 = list2.head

    while current1 or current2:
        if not current1:
            merged_current.next = current2
            break
        elif not current2:
            merged_current.next = current1
            break
        elif current1.data <= current2.data:
            merged_current.next = Node(current1.data)
            current1 = current1.next
        else:
            merged_current.next = Node(current2.data)
            current2 = current2.next

        merged_current = merged_current.next

    merged_list.head = merged_head.next
    return merged_list


if __name__ == "__main__":
    llist = LinkedList()

    # Вставляємо вузли в початок
    llist.insert_at_beginning(5)
    llist.insert_at_beginning(10)
    llist.insert_at_beginning(15)

    # Вставляємо вузли в кінець
    llist.insert_at_end(20)
    llist.insert_at_end(25)

    # Друк зв'язного списку
    print("Зв'язний список:")
    llist.print_list()
    print("Реверсивний список:")
    llist.reverse_list()
    llist.print_list()
    print("Відсортований список:")
    llist.insertion_sort()
    llist.print_list()

    # Створюємо другий список
    llist2 = LinkedList()

    # Вставляємо вузли в початок
    llist2.insert_at_beginning(15)
    llist2.insert_at_beginning(1)
    llist2.insert_at_beginning(5)

    # Сортуєм другий список
    print("Відсортований список:")
    llist2.insertion_sort()
    llist2.print_list()

    # Виводим об'єднаний відсортований список.
    print("Об'єднаний відсортований список.:")
    new_list = merge_sorted_lists(llist, llist2)
    new_list.print_list()
