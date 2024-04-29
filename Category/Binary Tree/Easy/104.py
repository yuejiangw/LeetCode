# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """ recursion """
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

from collections import deque
from typing import Optional
class Solution:
    """ 迭代法，采用层序遍历 """
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        if not root:
            return res
        queue = deque()
        queue.append(root)
        while queue:
            length = len(queue)
            for _ in range(length):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res += 1
        return res
