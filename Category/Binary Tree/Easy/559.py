"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

# BFS
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        queue = deque([root])
        res = 0
        while queue:
            l = len(queue)
            for _ in range(l):
                node = queue.popleft()
                for child in node.children:
                    queue.append(child)
            res += 1
        return res

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        # T: O(n), S: O(n)
        def get_depth(root):
            if not root:
                return 0
            depth = 0
            for i in range(len(root.children)):
                depth = max(depth, get_depth(root.children[i]))
            return depth + 1
        return get_depth(root)