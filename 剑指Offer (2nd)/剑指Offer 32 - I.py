# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from typing import List
class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        queue = deque()
        queue.append(root)
        while queue:
            length = len(queue)
            for _ in range(length):
                node = queue.popleft()
                res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res
