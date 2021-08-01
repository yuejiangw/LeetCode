# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        queue = deque()
        queue.append(root)
        res = []
        while queue:
            row = []
            for i in range(len(queue)):
                node = queue.popleft()
                row.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(row)
        return [max(x) for x in res]