# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''
        if not root.left and not root.right:
            return str(root.val)

        left = self.tree2str(root.left)
        right = self.tree2str(root.right)

        # 空的右子树可以省略
        if root.left and not root.right:
            return str(root.val) + "(" + left + ")"
        # 空的左子树不能省略
        if not root.left and root.right:
            return str(root.val) + '()' + '(' + right + ')'
        # 左右子树都不空
        return str(root.val) + '(' + left + ')' + '(' + right + ')'
