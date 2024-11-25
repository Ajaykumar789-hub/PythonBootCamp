# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
 
def postorder_traversal(root):
    """
    Function to perform postorder traversal of a binary tree.
    :param root: TreeNode -> root of the binary tree
    :return: List[int] -> list of nodes in postorder
    """
    if not root:
        return []
 
    stack1 = [root]  # Initialize stack1 with root
    stack2 = []  # This will store nodes in reverse postorder
    result = []
 
    # Traverse the tree
    while stack1:
        node = stack1.pop()  # Pop from stack1
        stack2.append(node)  # Push onto stack2
        
        # Push the left and right children onto stack1
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
 
    # Collect the nodes from stack2 to get postorder
    while stack2:
        result.append(stack2.pop().val)  # Pop from stack2 and append to result
    
    return result
 
# Helper function to display the postorder traversal (for debugging)
def display_postorder(root):
    print(postorder_traversal(root))
 
# Example usage (can be removed)
# root = TreeNode(1)
# root.right = TreeNode(2)
# root.right.left = TreeNode(3)
# display_postorder(root)
