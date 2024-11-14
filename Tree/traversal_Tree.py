from genericTressInput import predefined_generic_tree_inputs

root1, root2, root3 = predefined_generic_tree_inputs()

def preOrder_traversal(root):
    if root == None:
        return None
    print(root.data, end = " ")
    for child in root.children:
        preOrder_traversal(child)

#preOrder_traversal(root1)
# preOrder_traversal(root2)
preOrder_traversal(root3)

print("\n")
def postOder_traversal(root):
    if root == None:
        return None
    for child in root.children:
        postOder_traversal(child)
    print(root.data, end = " ")

# postOder_traversal(root1)
# postOder_traversal(root2)
postOder_traversal(root3)
