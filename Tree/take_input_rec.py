from common import TreeNode, print_tree_detailed

def take_input():
    data  = int(input("Enter the Data for Node:"))
    node = TreeNode(data)

    num_child = int(input(f"Enter num of children for {data}:"))

    for _ in range(num_child):
        child = take_input()
        node.children.append(child)
    return node

root = take_input()
print_tree_detailed(root)
