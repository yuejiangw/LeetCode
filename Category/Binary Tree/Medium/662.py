# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
from collections import deque


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        if not root:
            return res
        # 二叉树性质：left = 2 * root   right = 2 * root + 1
        # BFS，每次将 (编号，节点) 元组入队列，根据同层最大编号和最小编号的差值求 width
        queue = deque([(1, root)])
        while queue:
            length = len(queue)
            start, end = 0, 0
            for i in range(length):
                idx, node = queue.popleft()
                if i == 0:
                    start = idx
                if i == length - 1:
                    end = idx
                if node.left:
                    queue.append((2 * idx, node.left))
                if node.right:
                    queue.append((2 * idx + 1, node.right))
            res = max(res, end - start + 1)
        return res
