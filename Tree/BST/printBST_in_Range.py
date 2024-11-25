

def printBSTRange(root, low, high):
    if root is None:
        return
    if low<root.data:
        printBSTRange(root.left, low, high)
    if low<=root.data<=high:
        print(root.data, end =" ")
    if root<high:
        printBSTRange(root.right, low, high)