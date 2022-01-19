# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
from typing import List

class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        res = defaultdict(list)
        # 后序遍历获取高度，叶子节点高度为1
        def get_height(root):
            if not root:
                return 0
            left = get_height(root.left)
            right = get_height(root.right)
            height = max(left, right) + 1
            # 按照高度划分叶子结点，插入哈希表
            res[height].append(root.val)
            return height

        get_height(root)
        return list(res.values())
