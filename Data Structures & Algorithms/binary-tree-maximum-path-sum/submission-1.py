# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxVal = float('-inf')
        def maxx(node):
            nonlocal maxVal
            if not node:
                return 0
            leftV = max(maxx(node.left), 0)
            rightV = max(maxx(node.right), 0)
            currentV = leftV + rightV + node.val
            maxVal = max(maxVal, currentV)
            return node.val + max(leftV, rightV)
        maxx(root)
        return maxVal

        