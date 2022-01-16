# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict
from typing import List, Optional


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return root
        queue = deque()
        queue.append([root, 0])
        res = defaultdict(list)
        while queue:
            length = len(queue)
            for _ in range(length):
                node, col = queue.popleft()
                res[col].append(node.val)
                if node.left:
                    queue.append([node.left, col - 1])
                if node.right:
                    queue.append([node.right, col + 1])
        result = []
        key = sorted(list(res.keys()))
        for k in key:
            result.append(res[k])
        return result
