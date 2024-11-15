from preDefinedBT import predefined_binary_tree_inputs
root1,root2,root3 = predefined_binary_tree_inputs()
def height(root):
    if root == None:
        return 0
    left_height = height(root.left)
    right_height = height(root.right)

    height_of_tree = 1 + max(left_height, right_height)
    return height_of_tree

def diameter_of_tree(root):
    if root == None:
        return 0
    leftheight = height(root.left)
    rightheight = height(root.left)

    left_dia = diameter_of_tree(root.left)
    right_dia = diameter_of_tree(root.right)

    return max(leftheight, rightheight, left_dia, right_dia)

print(diameter_of_tree(root1))