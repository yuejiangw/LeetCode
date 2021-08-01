"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        queue = deque()
        queue.append(root)
        tree = []
        while queue:
            row = deque()
            for i in range(len(queue)):
                node = queue.popleft()
                row.append(node)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            tree.append(row)
        for row in tree:
            for i in range(len(row)):
                if i == len(row) - 1:
                    row[i].next = None
                else:
                    row[i].next = row[i + 1]
        return root