from common import TreeNode, print_tree_detailed
from collections import deque

def take_input_level_wise():

    data = int(input("Enter root data: "))
    root = TreeNode(data)

    queue = deque([root])

    while len(queue) != 0:
        current_node = queue.popleft()
        num_of_children = int(input(f"Enter the number of children for Node: " + str(current_node.data)))
        for i in range(num_of_children):
            child_data = int(input(f"Enter child data for {i+1} for current_Node: {current_node.data}: "))
            child_node = TreeNode(child_data)
            current_node.children.append(child_node)
            queue.append(child_node)
    return root

root = take_input_level_wise()
print_tree_detailed(root)

        