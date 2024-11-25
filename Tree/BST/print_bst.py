
class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def print_bst(root):
    if root is None:
        return
    print_bst(root.left)
    print(root.data, end = " ")
    print_bst(root.data)