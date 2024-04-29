# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

# 2024-04-26
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # 我们不需要存储每一层的节点，只需要存储每一层的和
        res = []
        queue = deque()
        if root:
            queue.append(root)
        while queue:
            l = len(queue)
            level = 0
            for _ in range(l):
                node = queue.popleft()
                level += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level / l)
        return res


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        
        def get_avg(nums):
            return sum(nums) / len(nums)

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
        return [get_avg(x) for x in res]