# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

# 2024-04-26
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # 不需要存储每一层的节点，只需要存储每一层的最后一个节点
        # 空间复杂度可以优化为 O(2^h)，h 为树的高度
        res = []
        queue = deque()
        if root:
            queue.append(root)
        while queue:
            l = len(queue)
            for i in range(l):
                node = queue.popleft()
                if i == l - 1:
                    res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        # 空间复杂度为 O(n)，不是最优解
        if not root:
            return []
        queue = deque()
        queue.append(root)
        res = []
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(level)
        return [x[-1] for x in res]