# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        maxx = float('-inf')
        count = 0

        def getgoodnodes(node, maxx):
            nonlocal count
            if not node:
                return 
            if node.val >= maxx:
                count += 1
                maxx = node.val
            getgoodnodes(node.left, maxx)
            getgoodnodes(node.right, maxx)

        getgoodnodes(root, maxx)
        return count

        
        
        
                            


        