# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        self.resL, self.resR= 0, 0
        def height(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            left = height(root.left)
            if left == -1:
                return -1
            right = height(root.right)
            if right == -1:
                return -1

            if abs(left-right) > 1:
                return -1
            else:
                return max(left, right) + 1

        if height(root) == -1:
            return False
        
        return True


        
