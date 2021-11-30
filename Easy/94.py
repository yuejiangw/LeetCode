from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root):
        """非递归版"""
        stack = []
        res = []
        curr = root
        while curr is not None or len(stack) > 0:
            if curr is not None:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                res.append(curr.val)
                curr = curr.right
        return res

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """递归版"""
        def recursion(root):
            if not root:
                return
            recursion(root.left)
            res.append(root.val)
            recursion(root.right)
        res = []
        recursion(root)
        return res