# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        nLeft = self.maxDepth(root.left)
        nRight = self.maxDepth(root.right)
        return max(nLeft, nRight) + 1