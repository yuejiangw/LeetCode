# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        # root 为二叉树中的最小值，我们要找到一个严格小于 root.val 的尽可能大的值
        min_val = root.val
        res = -1
        
        def traversal(root):
            nonlocal res
            if not root:
                return
            if root.val > min_val:
                res = root.val if res == -1 else min(res, root.val)
            traversal(root.left)
            traversal(root.right)
        traversal(root)
        return res
