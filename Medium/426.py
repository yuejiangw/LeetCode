"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
from collections import deque


"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
# Recursive
class Solution:
    
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        '''
        中序遍历
        T: O(N), S: O(N)
        '''
        if not root:
            return None

        head = None
        pre = None
        
        def traversal(root):
            nonlocal head, pre
            if not root:
                return
            
            traversal(root.left)

            if not head:
                head = root
            else:
                pre.right= root
                root.left = pre

            pre = root

            traversal(root.right)
        
        traversal(root)
        head.left = pre
        pre.right = head
        return head

# Iterative
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None

        stack = deque()
        head = None
        pre = None

        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            if not head:
                head = root
            else:
                pre.right = root
                root.left = pre
            pre = root
            root = root.right

        head.left = pre
        pre.right = head

        return head
