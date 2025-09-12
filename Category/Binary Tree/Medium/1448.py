# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: Optional[TreeNode]) -> int:
        res = 0
        # dfs - 下探的同时传递当前路径的最大值
        def dfs(root, maxVal):
            nonlocal res
            if not root:
                return
            if root.val >= maxVal:
                res += 1
            maxVal = max(maxVal, root.val)
            dfs(root.left, maxVal)
            dfs(root.right, maxVal)
        
        dfs(root, root.val)
        return res