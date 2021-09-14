"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def get_depth(root):
            if not root:
                return 0
            depth = 0
            for i in range(len(root.children)):
                depth = max(depth, get_depth(root.children[i]))
            return depth + 1
        return get_depth(root)