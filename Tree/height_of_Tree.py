from genericTressInput import predefined_generic_tree_inputs

def height_of_Tree(root):
    if root == None:
        return 0
    height, max_of_height = 1,0
    for child in root.children:
        max_of_height = max(max_of_height, height_of_Tree(child))
    height = height + max_of_height
    return height
root1, root2, root3 = predefined_generic_tree_inputs()

print(height_of_Tree(root1))
print(height_of_Tree(root2))
print(height_of_Tree(root3))
    