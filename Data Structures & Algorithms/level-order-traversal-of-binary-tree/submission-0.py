# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        out = []
        if root is None:
            return out
        queue = deque()
        queue.append(root)
        while queue:
            level_size = len(queue)
            curr_level = []
            for i in range(level_size):
                node = queue.popleft()
                curr_level.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            out.append(curr_level)
        return out