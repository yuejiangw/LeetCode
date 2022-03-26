"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        head = None
        pre = None

        def traverse(root):
            nonlocal pre, head
            if not root:
                return
            traverse(root.left)
            if pre:
                pre.right = root
                root.left = pre
            else:
                head = root
            pre = root
            traverse(root.right)
        
        if not root:
            return None
        traverse(root)
        head.left = pre
        pre.right = head
        return head