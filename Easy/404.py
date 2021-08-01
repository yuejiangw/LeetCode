# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 0
        if root.left is not None and root.left.left is None and root.left.right is None:
            res += root.left.val
        return res + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)