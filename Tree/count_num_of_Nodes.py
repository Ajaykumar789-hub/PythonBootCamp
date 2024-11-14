from genericTressInput import predefined_generic_tree_inputs

def count_nodes(root):
    if root == None:
        return 0
    numOfNodes = 1
    for child in root.children:
        numOfNodes = numOfNodes + count_nodes(child)
    return numOfNodes

root1, root2, root3 = predefined_generic_tree_inputs()

print(count_nodes(root1))
print(count_nodes(root2))
print(count_nodes(root3))