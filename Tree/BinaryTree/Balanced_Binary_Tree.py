# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def height(self, root):
        if root is None:
            return 0
        left_height = self.isBalanced(root.left)
        right_height = self.isBalanced(root.right)
        if abs(left_height - right_height) > 1 or left_height < 0 or right_height < 0:
            return -1
        return 1 + max(left_height, right_height)
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        return (self.height(root) >= 0)
        