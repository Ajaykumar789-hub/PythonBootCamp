
def search_bst(root, value):
    if root is None:
        return
    if root.data == value:
        return root
    if root.data>value:
        search_bst(root.left, value)
    elif root.data<value:
        search_bst(root.right, value)
    