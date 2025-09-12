# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        path = 0
        res = 0

        def backtracking(root):
            nonlocal path
            nonlocal res
            if not root:
                return
            path = path * 10 + root.val
            if not root.left and not root.right:
                res += path
            if root.left:
                backtracking(root.left)
            if root.right:
                backtracking(root.right)
            path = path // 10
        
        backtracking(root)
        return res
