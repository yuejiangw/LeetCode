# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List


class Solution:
    def get_height(self, root):
        if not root:
            return 0
        return 1 + max(self.get_height(root.left), self.get_height(root.right))

    def printTree(self, root: TreeNode) -> List[List[str]]:
        if not root:
            return []
        height = self.get_height(root)
        width = 2 ** height - 1
        res = [[''] * width for _ in range(height)]

        def fill(root, i, l, r):
            """ 递归填充 res 数组
            root: 当前节点
            i: 当前深度
            l: 左边界
            r: 右边界
            """
            if not root:
                return
            mid = l + (r - l) // 2
            res[i][mid] = str(root.val)
            # 递归填充左子树
            fill(root.left, i + 1, l, mid - 1)
            # 递归填充右子树
            fill(root.right, i + 1, mid + 1, r)

        fill(root, 0, 0, width)
        return res
