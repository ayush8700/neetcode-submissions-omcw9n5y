# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def getHeight(node):
            if not node:
                return 0

            left_h = getHeight(node.left)
            right_h = getHeight(node.right)

            if abs(left_h - right_h) > 1:
                return -1
            
            if left_h == -1 or right_h == -1:
                return -1
            
            return 1 + max(right_h, left_h)
        
        return getHeight(root) != -1
        