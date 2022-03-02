# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float('-inf')

        def one_side_max(root):
            if not root:
                return 0
            
            left_max_sum = max(0, one_side_max(root.left))
            right_max_sum = max(0, one_side_max(root.right))
            # 后序遍历位置, 顺便更新最大路径和
            path_max_sum = root.val + left_max_sum + right_max_sum
            self.res = max(self.res, path_max_sum)
            # 实现函数定义，左右子树的最大单边路径和加上根节点的值
            # 就是从根节点 root 为起点的最大单边路径和
            return max(left_max_sum, right_max_sum) + root.val

        if not root:
            return 0
        one_side_max(root)
        return self.res
