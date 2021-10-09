# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = deque()
        queue.append(root)
        count = 1
        while queue:
            length = len(queue)
            path = []
            for _ in range(length):
                node = queue.popleft()
                path.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if count % 2 == 1:
                res.append(path)
            else:
                res.append(path[::-1])
            count += 1
        return res