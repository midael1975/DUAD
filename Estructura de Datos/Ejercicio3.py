class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def print_vertical(self, level):
        # Print right subtree first (appears on top)
        if self.right is not None:
            self.right.print_vertical(level + 1)

        # Indentation based on depth
        spaces = ""
        i = 0
        while i < level:
            spaces = spaces + "    "
            i = i + 1

        print(spaces + str(self.value))

        # Print left subtree (appears below)
        if self.left is not None:
            self.left.print_vertical(level + 1)


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.root.insert(value)

    def print_tree(self):
        if self.root is None:
            print("Tree is empty")
        else:
            self.root.print_vertical(0)


# Example usage
tree = BinaryTree()
tree.insert(8)
tree.insert(3)
tree.insert(10)
tree.insert(1)
tree.insert(6)
tree.insert(14)
tree.insert(4)
tree.insert(7)
tree.insert(13)

tree.print_tree()





