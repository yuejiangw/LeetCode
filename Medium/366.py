# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List
from collections import OrderedDict
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        res = OrderedDict()

        def max_height(root: TreeNode):
            if not root:
                return 0
            # 后序遍历获取高度，叶子节点高度为1
            left = max_height(root.left)
            right = max_height(root.right)
            h = max(left, right) + 1
            if not res.get(h):
                res[h] = []
            # 按照高度划分叶子节点，存入哈希表
            res[h].append(root.val)
            return h

        max_height(root)
        return list(res.values())
