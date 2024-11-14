class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []

root = TreeNode(1)
child1 = TreeNode(2)
child2 = TreeNode(3)
child3 = TreeNode(4)

root.children.append(child1)
root.children.append(child2)
root.children.append(child3)

def print_tree(root):
    print(root.data)

    for child in root.children:
        print_tree(child)

# print(print_tree(root))

## Problem: Multiple Tree can have same output

def print_tree_detailed(root):
    if root == None:
        return
    print(f"{root.data}:", end= "")

    for child in root.children:
        print(child.data, end = ",")
    print()
    for child in root.children:
        print_tree_detailed(child)

# print(print_tree_detailed(root))

root = TreeNode(1)
child1 = TreeNode(2)
child2 = TreeNode(3)
child3 = TreeNode(4)
root.children.append(child1)
child1.children.append(child2)
root.children.append(child3)

print(print_tree_detailed(root))
