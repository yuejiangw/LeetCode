# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        path = []
        def traversal(root):
            if not root:
                return
            traversal(root.left)
            path.append(root.val)
            traversal(root.right)
        traversal(root)
        res = float('inf')
        for i in range(1, len(path)):
            res = min(res, path[i] - path[i - 1])
        return res