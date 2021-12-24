# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        res = []
        path = []

        def backtracking(root):
            path.append(str(root.val))
            if not root.left and not root.right:
                res.append(int(''.join(path)))
                return
            if root.left:
                backtracking(root.left)
                path.pop(-1)
            if root.right:
                backtracking(root.right)
                path.pop(-1)
        if not root:
            return 0
        backtracking(root)
        return sum(res)
