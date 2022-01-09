# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res = []
        queue = deque([root])
        count = 0
        while queue:
            length = len(queue)
            level = []
            for _ in range(length):
                node = queue.popleft()
                level.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            if count % 2 == 0:
                res.append(level)
            else:
                res.append(level[::-1])
            count += 1
        return res