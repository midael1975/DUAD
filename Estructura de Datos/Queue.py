class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Queue:
    def __init__(self, head=None):
        self.front = head
        self.rear = None

    def is_empty(self):
        return self.front is None
    
    def print_queue(self):
        current = self.front
        while current:
            print(current.value, end=' ')
            current = current.next
        print()

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return value

    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.front.value

    def size(self):
        count = 0
        current = self.front
        while current:
            count += 1
            current = current.next
        return count
# Example usage
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  # Output: 1
print(queue.peek())    # Output: 2
print(queue.size())
queue.print_queue()    # Output: 2 3