from preDefinedBT import predefined_binary_tree_inputs, BinaryTreeNode
root1,root2,root3 = predefined_binary_tree_inputs()

def construct_Ino_Pre(inOrder, preOrder, inS, inE, preS, preE):

    if inS>inE or preS > preE: # Base Condtion
        return None
    root_data = preOrder[preS]
    root = BinaryTreeNode(root_data)

    rootIndex = -1
    for i in range(inS, inE+1):
        if inOrder[i] == root_data:
            rootIndex = i
            break
    if rootIndex == -1:
        print("root not found")
        return None
    
    linS = inS
    linE = rootIndex - 1
    lpreS = preS + 1
    lpreE = linE - linS + lpreS

    rinS = rootIndex + 1
    rinE =  inE
    rpreS = lpreE + 1
    rpreE =  preE

    root.left = construct_Ino_Pre(inOrder, preOrder, linS, linE, lpreS, lpreE)
    root.right = construct_Ino_Pre(inOrder, preOrder, rinS, rinE, rpreS, rpreE)

    return root

## solved in Leetcode: 105
    



