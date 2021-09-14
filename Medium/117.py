"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        queue = deque()
        queue.append(root)
        while queue:
            size = len(queue)
            pre = None
            for i in range(size):
                if i == 0:
                    node = queue.popleft()
                    pre = node
                else:
                    node = queue.popleft()
                    pre.next = node
                    pre = node
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            pre.next = None
        return root