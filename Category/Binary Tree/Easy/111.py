# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        """迭代"""
        if not root:
            return 0
        queue = deque()
        queue.append(root)
        depth = 0
        while queue:
            depth += 1
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if node.left is None and node.right is None:
                    return depth
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        return depth

    def minDepth(self, root):
        """递归"""
        def getDepth(node):
            if not node:
                return 0
            if node.left is not None and node.right is None:
                return 1 + getDepth(node.left)
            if node.right is not None and node.left is None:
                return 1 + getDepth(node.right)    
            return min(getDepth(node.left), getDepth(node.right)) + 1
        if not root:
            return 0
        return getDepth(root)

from typing import Optional
class Solution:
    """另外一种递归写法，不需要构建辅助函数"""
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        elif not root.left and not root.right:
            return 1
        elif not root.left:
            return self.minDepth(root.right) + 1
        elif not root.right:
            return self.minDepth(root.left) + 1
        else:
            return min(self.minDepth(root.right), self.minDepth(root.left)) + 1

class Solution:
    """ bfs """
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = deque([root])
        depth = 1
        while queue:
            length = len(queue)
            for _ in range(length):
                node = queue.popleft()
                if node.left is None and node.right is None:
                    return depth
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1
        return depth
