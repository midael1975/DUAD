class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_back(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def delete(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def print_list(self):
        current = self.head
        if current is None:
            print("List is empty")
            return
        while current is not None:
            print(current.data, end=' ')
            current = current.next
        print()

# Example usage
llist = LinkedList()
llist.insert_back(1)
llist.insert_back(2)
llist.insert_back(3)
llist.insert_front(0)
llist.print_list()  # Output: 0 1 2 3 
llist.delete(2)
llist.print_list()  # Output: 0 1 3 
llist.delete(0)
llist.print_list()  # Output: 1 3
llist.delete(3)
llist.print_list()  # Output: 1
