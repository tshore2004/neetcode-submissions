# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root

        if curr is None:
            return None
        if curr is p or curr is q:
            return curr
        left = self.lowestCommonAncestor(curr.left, p, q)
        right = self.lowestCommonAncestor(curr.right, p, q)
        if left is not None and right is not None:
            return curr
        elif left is None and right is None:
            return None
        elif left is None:
            return right
        elif right is None:
            return left

