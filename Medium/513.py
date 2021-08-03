# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        queue = deque()
        queue.append(root)
        row = []
        while queue:
            row = []
            for i in range(len(queue)):
                node = queue.popleft()
                row.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        return row[0]