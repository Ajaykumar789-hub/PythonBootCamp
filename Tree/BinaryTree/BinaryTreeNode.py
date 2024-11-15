class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)

def print_binary_tree(root):
    if root == None:
        return
    print(root.data)
    print_binary_tree(root.left)
    print_binary_tree(root.right)

# print_binary_tree(root)

def print_bt_detaild(root):
    if root == None:
        return
    print(root.data, end= ": ")
    if root.left:
        print(f"L-->{root.left.data}", end=",")
    else:
        print("L-->None", end=",")
    
    if root.right:
        print(f"R-->{root.right.data}", end=",")
    else:
        print("R-->None", end=",")

    print_bt_detaild(root.left)
    print_bt_detaild(root.right)

from preDefinedBT import predefined_binary_tree_inputs
root1,root2,root3 = predefined_binary_tree_inputs()
print_bt_detaild(root1)
