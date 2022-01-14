# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        x_level, x_parent, y_level, y_parent = None, None, None, None
        # Add tuples into queue: (node, parent)
        queue = deque([(root, None)])
        depth = 0
        while queue:
            length = len(queue)
            for _ in range(length):
                node, parent = queue.popleft()
                if node.val == x:
                    x_level, x_parent = depth, parent
                if node.val == y:
                    y_level, y_parent = depth, parent
                if node.left:
                    queue.append((node.left, node))
                if node.right:
                    queue.append((node.right, node))
            depth += 1
        return x_level == y_level and x_parent != y_parent
