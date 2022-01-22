# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        res = 0

        def traverse(root: TreeNode, parent_val: int):
            """ 以 root 为根的这棵二叉树中，从 root 开始值为 parent_val 的最长树枝长度 """
            nonlocal res
            if not root:
                return 0
            left = traverse(root.left, root.val)
            right = traverse(root.right, root.val)

            res = max(res, left + right)
            if root.val != parent_val:
                return 0
            return 1 + max(left, right)

        if not root:
            return 0
        traverse(root, root.val)
        return res
