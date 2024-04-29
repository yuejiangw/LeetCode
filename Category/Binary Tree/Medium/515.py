# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 2024-04-26
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # 不需要存储每一层的节点，只需要存储每一层的最大值
        if not root:
            return []
        res = []
        queue = deque([root])
        while queue:
            l = len(queue)
            level = float('-inf')
            for _ in range(l):
                node = queue.popleft()
                level = max(level, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)
        return res

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