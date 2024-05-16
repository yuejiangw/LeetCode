# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        res = 0
        while queue:
            l = len(queue)
            for i in range(l):
                node = queue.popleft()
                if i == 0:
                    res = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res
    
class Solution:
    res = None
    max_depth = float('-inf')
    
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # 递归法, 深度最大的叶子节点一定是最后一行, 第一个遇到的深度最大的节点一定是最底层最左边的节点
        def traversal(root, depth):
            if not root.left and not root.right:
                if depth > self.max_depth:
                    self.max_depth = depth
                    self.res = root.val
            if root.left:
                depth += 1
                traversal(root.left, depth)    
                depth -= 1
            if root.right:
                depth += 1
                traversal(root.right, depth)
                depth -= 1
        
        traversal(root, 0)
        return self.res