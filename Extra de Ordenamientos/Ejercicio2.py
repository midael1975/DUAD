class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        self.prev = None


class DoubleEndedQueue:
    def __init__(self):
        self.left = None
        self.right = None

    def is_empty(self):
        return self.left is None

    def push_left(self, value):
        new_node = Node(value)
        if self.left is None:
            self.left = new_node
            self.right = new_node
        else:
            new_node.next = self.left
            self.left.prev = new_node
            self.left = new_node

    def push_right(self, value):
        new_node = Node(value)
        if self.right is None:
            self.left = new_node
            self.right = new_node
        else:
            new_node.prev = self.right
            self.right.next = new_node
            self.right = new_node

    def pop_left(self):
        if self.left is None:
            raise Exception("Deque is empty")
        removed_value = self.left.value
        self.left = self.left.next
        if self.left is not None:
            self.left.prev = None
        else:
            self.right = None

        return removed_value

    def pop_right(self):
        if self.right is None:
            raise Exception("Deque is empty")
        removed_value = self.right.value
        self.right = self.right.prev
        if self.right is not None:
            self.right.next = None
        else:
            self.left = None

        return removed_value

    def print_deque(self):
        current = self.left
        while current is not None:
            print(current.value, end=' ')
            current = current.next
        print()

    def bubble_sort(self):
        if self.left is None:
            return

        swapped = True
        while swapped:
            swapped = False
            current = self.left

            while current.next is not None:
                if current.value > current.next.value:
                    current.value, current.next.value = current.next.value, current.value
                    swapped = True
                current = current.next

# Example usage
deque = DoubleEndedQueue()
deque.push_left(1)
deque.push_left(2)
deque.push_right(3)
deque.push_right(4)
# deque.print_deque()  # Output: 2 1 3 4
# print(deque.pop_left())  # Output: 2
# print(deque.pop_right())  # Output: 4
# deque.print_deque()  # Output: 1 3

print("Before sorting:")
deque.print_deque()  # Output: 2 1 3 4
deque.bubble_sort()
print("After sorting:")
deque.print_deque() # Output: 1 2 3 4