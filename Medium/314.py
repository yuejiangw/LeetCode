# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict
from typing import List, Optional


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """BFS"""
        # T: O(n), S: O(n)
        if not root:
            return []
        nodes = defaultdict(list)
        min_val, max_val = float('inf'), float('-inf')
        queue = deque([(0, root)])
        while queue:
            num, node = queue.popleft()
            nodes[num].append(node.val)
            min_val = min(min_val, num)
            max_val = max(max_val, num)
            if node.left:
                queue.append((num - 1, node.left))
            if node.right:
                queue.append((num + 1, node.right))
        res = []
        for i in range(min_val, max_val + 1):
            res.append(nodes[i])
        return res
    

    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """ DFS """
        nodes = []
        
        def traversal(root, row, col):
            if not root:
                return 
            nodes.append([root.val, row, col])
            traversal(root.left, row + 1, col - 1)
            traversal(root.right, row + 1, col + 1)
        
        traversal(root, 0, 0)
        nodes = sorted(nodes, key=lambda x: (x[2], x[1]))
        i = 0
        res = []
        while i < len(nodes):
            col = [nodes[i][0]]
            j = i + 1
            while j < len(nodes) and nodes[j][2] == nodes[i][2]:
                col.append(nodes[j][0])
                j += 1
            res.append(col)
            i = j
        return res