# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root, None)
        queue = deque([root])
        curr_depth = 1
        while queue:
            l = len(queue)
            for _ in range(l):
                node = queue.popleft()
                if curr_depth == depth - 1:
                    a, b = TreeNode(val), TreeNode(val)
                    a.left = node.left
                    b.right = node.right
                    node.left = a
                    node.right = b
                else:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            curr_depth += 1
        
        return root