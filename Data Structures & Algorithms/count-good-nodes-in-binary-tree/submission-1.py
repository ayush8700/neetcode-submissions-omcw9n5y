# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        maxx = float('-inf')
        
        def get(node, maxx):
            if not node:
                return 
            nonlocal count
            if maxx <= node.val:
                maxx = max(maxx, node.val)
                count += 1
            get(node.left, maxx)
            get(node.right, maxx)
            return 
        get(root, maxx)
        return count
            
            
        