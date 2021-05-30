
class Node:

    def __init__(self, value=0, left_node=None, right_node=None):
        self.val = value
        self.left = left_node
        self.right = right_node

    def __str__(self):
        return f'Node id: {repr(self)}, value: {self.val}, left: {repr(self.left)}, right: {repr(self.right)}';


class LeftView:

    def __init__(self, root_node=None):
        self.root = root_node
        self.left_view = [-1] * 10
        self.create_left_view(self.root, 0)

    def create_left_view(self, node=None, lvl=0):
        if node.left is not None:
            self.create_left_view(node.left, lvl+1)
        elif node.right is not None:
            self.create_left_view(node.right, lvl+1)
        else:
            self.left_view[lvl] = node.val

    def __str__(self):
        return f"LeftView of tree rooted at {repr(self.root)} is {self.left_view}"


if __name__ == "__main__":
    t1_root = Node(1, Node(2), Node(3))
    print(t1_root)
    print(t1_root.left)

    print(LeftView(t1_root))
    #print(LeftView(None))

