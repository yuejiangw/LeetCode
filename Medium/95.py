# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def build(low, high):
            res = []
            if low > high:
                res.append(None)
                return res
            # 穷举所有 root 可能的值
            for i in range(low, high + 1):
                # 根据 bst 性质递归构造左右子树
                left = build(low, i - 1)
                right = build(i + 1, high)
                # 已知左子树可能有 left 个，右子树可能有 right 个，则以 i 为根节点
                # 一共可以产生 left * right 个 bst 序列
                for left_node in left:
                    for right_node in right:
                        root = TreeNode(i)
                        root.left = left_node
                        root.right = right_node
                        res.append(root)
            return res
        return build(1, n)