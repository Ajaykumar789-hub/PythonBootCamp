class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []

def print_tree_detailed(root):
    if root == None:
        return
    print(f"{root.data}:", end= "")

    for child in root.children:
        print(child.data, end = ",")
    print()
    for child in root.children:
        print_tree_detailed(child)