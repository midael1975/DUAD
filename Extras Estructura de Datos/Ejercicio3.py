class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def print_forward(self):
        current = self.head
        elements = []
        while current is not None:
            elements.append(current.data)
            current = current.next
        return elements

    def print_backward(self):
        current = self.tail
        elements = []
        while current is not None:
            elements.append(current.data)
            current = current.prev
        return elements

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                if current == self.head:
                    self.head = current.next
                    if self.head is not None:
                        self.head.prev = None
                elif current == self.tail:
                    self.tail = current.prev
                    if self.tail is not None:
                        self.tail.next = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                return
            current = current.next

# Example usage
dll = DoubleLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
print(dll.print_forward())  # Output: [1, 2, 3]
print(dll.print_backward()) # Output: [3, 2, 1]
dll.prepend(0)
print(dll.print_forward())  # Output: [0, 1, 2, 3]
dll.delete(2)
print(dll.print_forward())  # Output: [0, 1, 3]
dll.delete(0)
print(dll.print_forward())  # Output: [1, 3]
dll.delete(3)
print(dll.print_forward())  # Output: [1]
dll.delete(1)
print(dll.print_forward())  # Output: []
print(dll.print_backward()) # Output: []
dll.append(1)
print(dll.print_forward())  # Output: [1]