# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
 
def preorder_traversal(root):
    """
    Function to perform preorder traversal of a binary tree.
    :param root: TreeNode -> root of the binary tree
    :return: List[int] -> list of nodes in preorder
    """
    # Initialize an empty stack and result list
    if not root:
        return []
 
    stack = [root]
    result = []
 
    # Traverse the tree
    while stack:
        node = stack.pop()  # Pop from stack (current node)
        result.append(node.val)  # Visit the current node (add to result)
        
        # Push the right child first so that the left child is processed first
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    return result
 
# Helper function to display the preorder traversal (for debugging)
def display_preorder(root):
    print(preorder_traversal(root))
 
# Example usage (can be removed)
# root = TreeNode(1)
# root.right = TreeNode(2)
# root.right.left = TreeNode(3)
# display_preorder(root)
