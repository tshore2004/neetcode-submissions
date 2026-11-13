# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        curr = root
        maxRight = 0
        maxLeft = 0
        if curr == None:
            return 0
        
        maxLeft = self.maxDepth(curr.left)
        maxRight = self.maxDepth(curr.right)



        return max(maxRight, maxLeft) + 1