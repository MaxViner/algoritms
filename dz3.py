class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

class LinkedList:
    def __init__(self, head=None):
        self.head = head
    
    def add(self, value):
        new_node = Node(value)
        new_node.next_node = self.head
        self.head = new_node
    
    def reverse(self):
        prev_node = None
        current_node = self.head
        while current_node is not None:
            next_node = current_node.next_node
            current_node.next_node = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node
    
    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value, end=' ')
            current_node = current_node.next_node
        print()

# Пример использования
linked_list = LinkedList()
linked_list.add(1)
linked_list.add(2)
linked_list.add(3)
print("Исходный список:")
linked_list.print_list()

linked_list.reverse()
print("Список после разворота:")
linked_list.print_list()