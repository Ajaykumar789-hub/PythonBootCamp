from genericTressInput import predefined_generic_tree_inputs
root1, root2, root3 = predefined_generic_tree_inputs()

def sum_of_nodes(root):
    if root == None:
        return 0
    sum = root.data
    for child in root.children:
        sum = sum + sum_of_nodes(child)
    return sum

print(sum_of_nodes(root3))