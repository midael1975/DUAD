class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            raise Exception("Stack is empty")
        removed_data = self.top.data
        self.top = self.top.next
        return removed_data

    def print_stack(self):
        current = self.top
        while current is not None:
            print(current.data, end=' ')
            current = current.next
        print()

    def bubble_sort(self):
        if self.top is None:
            return

        swapped = True
        while swapped:
            swapped = False
            current = self.top

            while current.next is not None:
                if current.data > current.next.data:
                    current.data, current.next.data = current.next.data, current.data
                    swapped = True
                current = current.next

# Example usage
stack = Stack()
stack.push(5)
stack.push(1)
stack.push(4)
stack.push(2)
stack.push(3)
#stack.print_stack()  # Output: 3 2 1
# print(stack.pop())  # Output: 3
# print(stack.pop())  # Output: 2
# print(stack.pop())  # Output: 1
# print(stack.pop())  # Output: 4
# print(stack.pop())  # Output: 5

print("Before sorting:")
stack.print_stack()  # Output: 3 2 1 4 5

stack.bubble_sort()

print("After sorting:")
stack.print_stack() # Output: 1 2 3 4 5

