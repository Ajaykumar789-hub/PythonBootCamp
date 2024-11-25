class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def find_max(node):
    if node is None:
        return float('-inf')
    left_max = find_max(node.left)
    right_max= find_max(node.right)

    ans = max(left_max, right_max, node.data)
    return ans

def find_min(node):
    if node is None:
        return float('inf')
    left_min = find_min(node.left)
    right_min = find_min(node.right)

    ans = min(left_min, right_min, node.data)
    return ans
def checkBST(root):
    if root is None:
        return True
    left_max = find_max(root.left)
    right_min = find_min(root.right)

    left_bst = checkBST(root.left)
    right_bst = checkBST(root.right)

    ans = left_bst and right_bst and left_max < root.data and root.data < right_min
    return ans

