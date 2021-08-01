# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
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