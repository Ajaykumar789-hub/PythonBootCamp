from preDefinedBT import predefined_binary_tree_inputs
root1,root2,root3 = predefined_binary_tree_inputs()

def preOrder(root):
    if root is None:
        return
    print(root.data, end = " ")
    preOrder(root.left)
    preOrder(root.right)

def postOrder(root):
    if root is None:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.data, end = " ")

def inOrder(root):
    if root is None:
        return
    inOrder(root.left)
    print(root.data, end = " ")
    inOrder(root.right)

print("pre order\n")
print(preOrder(root1))
print("post order\n")
print(postOrder(root1))
print("in order\n")
print(inOrder(root1))