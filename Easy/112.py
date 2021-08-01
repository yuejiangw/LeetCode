# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        remain = targetSum - root.val
        if root.left is None and root.right is None:
            return remain == 0
        return self.hasPathSum(root.left, remain) or \
               self.hasPathSum(root.right, remain)
