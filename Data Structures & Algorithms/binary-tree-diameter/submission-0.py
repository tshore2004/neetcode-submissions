# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not hasattr(self, 'max_diameter'):
            self.max_diameter = 0

        curr = root
        left, right = 0, 0
        def height(node: Optional[TreeNode]):
            if node == None:
                return 0

            left = height(node.left)
            right = height(node.right)
            self.max_diameter = max(left + right, self.max_diameter)
            return max(left, right) + 1
        height(root)
        return self.max_diameter