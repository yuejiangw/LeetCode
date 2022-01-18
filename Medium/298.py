# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        res = 0

        def traverse(root, length, parent_val):
            nonlocal res
            if not root:
                return
            if parent_val + 1 == root.val:
                length += 1
            else:
                length = 1
            res = max(res, length)
            traverse(root.left, length, root.val)
            traverse(root.right, length, root.val)

        traverse(root, 1, float('inf'))
        return res
