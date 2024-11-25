from preDefinedBT import predefined_binary_tree_inputs, BinaryTreeNode
root1,root2,root3 = predefined_binary_tree_inputs()

def construct_bt_in_pos(inorder, postorder, inS, inE, posS, posE):
    if inS>inE or posS>posE:
        return None
    root_data = postorder[posE]
    root = BinaryTreeNode(root)

    rootIndex = -1
    for i in range(inS, inE+1):
        if inorder[i] == root_data:
            rootIndex = i
            break
    if rootIndex == -1:
        print("root not found")
        return None
    
    linS = inS
    linE =  rootIndex -1 
    lposS = posS
    lposE = linE - linS + lposS

    rinS = rootIndex + 1
    rinE = inE
    rposS = lposE + 1
    rposE = posE - 1

    root.left = construct_bt_in_pos(inorder, postorder, linS, linE, lposS, lposE)
    root.right = construct_bt_in_pos(inorder, postorder, rinS, rinE, rposS, rposE)

    return root

# Solved in leetcode 106