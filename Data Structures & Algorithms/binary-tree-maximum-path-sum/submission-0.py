# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxxVal = float('-inf')
        def maxx(node):
            nonlocal maxxVal
            if not node:
                return 0
            leftVal = max(maxx(node.left), 0)
            rightVal = max(maxx(node.right), 0)

            currentVal = node.val + leftVal + rightVal
            maxxVal = max(maxxVal, currentVal)
            return node.val + max(leftVal, rightVal)
        maxx(root)
        return maxxVal
    