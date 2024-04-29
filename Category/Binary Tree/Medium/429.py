"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
# 2024-04-26
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        # 使用 deque 作为队列优化时间复杂度
        res = []
        queue = deque()
        if root:
            queue.append(root)
        while queue:
            l = len(queue)
            level = []
            for _ in range(l):
                node = queue.popleft()
                level.append(node.val)
                for child in node.children:
                    queue.append(child)
            res.append(level)
        return res


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return
        queue = [root]
        res = []
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)
                if node.children:
                    queue += node.children
            res.append(level)
        return res