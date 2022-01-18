# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
class Solution:
    """ 迭代版本 """
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        res = 0
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                res = root.val
                break
            root = root.right
        return res


class Solution:
    """ 递归版本 """
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        rank = 0
        res = 0

        def traversal(root):
            nonlocal res, rank
            if not root:
                return
            traversal(root.left)
            rank += 1
            if k == rank:
                res = root.val
                return
            traversal(root.right)

        traversal(root)
        return res
