
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
        self.left_view = []
        self.create_left_view(self.root, 1)

    def create_left_view(self, node=None, lvl=1):
        if node is not None:
            # no one inserted value at this level yet
            if len(self.left_view) < lvl:
                self.left_view.append(node.val)
            self.create_left_view(node.left, lvl+1)
            self.create_left_view(node.right, lvl+1)

    def __str__(self):
        return f"LeftView of tree rooted at {repr(self.root)} is {self.left_view}"


if __name__ == "__main__":
    t1_root = Node(1, Node(2), Node(3))
    print(t1_root)
    print(t1_root.left)
    print(LeftView(t1_root))

    print()
    print(LeftView(None))

    print()
    t2_root = Node(1, Node(2, Node(4), Node(5)), Node(3))
    print(LeftView(t2_root))

    print()
    t3_root = Node(1, Node(2, None, Node(5)), Node(3, Node(6, None, Node(7))))
    print(LeftView(t3_root))

    print()
    t4_root = Node(1, None, Node(3, Node(6, None, Node(7))))
    print(LeftView(t4_root))

    print()
    t5_root = Node(1, Node(2), Node(3, Node(6, None, Node(7))))
    print(LeftView(t5_root))
