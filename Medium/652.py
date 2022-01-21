# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional
from collections import defaultdict


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        res = []
        count = defaultdict(int)

        def traverse(root):
            """ 按照后序遍历的方式以字符串表示出一个树的结构 """
            if not root:
                return '#'
            left = traverse(root.left)
            right = traverse(root.right)
            subtree = left + ',' + right + ',' + str(root.val)

            # 当前子树结构已经出现过一次，则加入结果集合
            freq = count[subtree]
            if freq == 1:
                res.append(root)
            count[subtree] += 1

            return subtree

        traverse(root)
        return res
