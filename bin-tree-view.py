
class Node:

    def __init__(self, value=0, left_node=None, right_node=None):
        self.val = value
        self.left = left_node
        self.right = right_node

    def __str__(self):
        return f'Node id: {repr(self)}, value: {self.val}, left: {repr(self.left)}, right: {repr(self.right)}';


if __name__ == "__main__":
    n2 = Node(2)
    print(n2)
    n3 = Node(3)
    print(n3)
    n1 = Node(1, Node(4), Node(5))
    print(n1)
    print(n1.left)
