
class Node:

    def __init__(self, v=0, l=None, r=None):
        self.val = v
        self.left = l
        self.right = r

    def print(self):
        print(f'Node id: { hex(id(self)) }, value: {self.val}')

if __name__ == "__main__":
    n1 = Node(1)
    n1.print()
