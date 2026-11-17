# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p and q:
            return False
        if not q and p:
            return False
        if q.val == p.val:
            qpL = self.isSameTree(q.left, p.left)
            qpR = self.isSameTree(q.right, p.right)
            if qpL and qpR:
                return True
            else:
                return False
        else:
            return False