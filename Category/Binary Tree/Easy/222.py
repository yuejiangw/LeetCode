# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # T: O(logN * logN), S: O(logN)
        if not root:
            return 0
        left, right = root.left, root.right
        left_depth, right_depth = 1, 1
        while left:
            left = left.left
            left_depth += 1
        while right:
            right = right.right
            right_depth += 1
        if left_depth == right_depth:
            return (2 ** left_depth) - 1
        return self.countNodes(root.left) + self.countNodes(root.right) + 1
