class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def sortedListBst(l1):
    if len(l1) == 0:
        return 
    mid = len(l1) // 2  # middle Index
    rootData = l1[mid]

    root = BSTNode(root)

    root.left = sortedListBst(l1[:mid])
    root.right = sortedListBst(l1[mid+1:])

    return root

