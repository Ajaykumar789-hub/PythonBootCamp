class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
 
def inorder_traversal(root):
    """
    Function to perform inorder traversal of a binary tree.
    :param root: TreeNode -> root of the binary tree
    :return: List[int] -> list of nodes in inorder
    """
    # Initialize an empty stack and an empty result list
    stack = []
    result = []
    current = root
 
    # Traverse the tree
    while current or stack:
        # Reach the leftmost node of the current node
        while current:
            stack.append(current)  # Push the node onto the stack
            current = current.left  # Move to the left child
        
        # Current must be None at this point
        current = stack.pop()  # Pop the node from the stack
        result.append(current.val)  # Append the node's value to the result list
        
        # Visit the right subtree
        current = current.right
 
    return result
 
# Helper function to display the inorder traversal (for debugging)
def display_inorder(root):
    print(inorder_traversal(root))
 
# Example usage (can be removed)
# root = TreeNode(1)
# root.right = TreeNode(2)
# root.right.left = TreeNode(3)
# display_inorder(root)
