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
        """ BFS """
        if not root:
            return root
        queue = deque()
        queue.append([root, 0])
        res = defaultdict(list)
        while queue:
            length = len(queue)
            for _ in range(length):
                node, col = queue.popleft()
                res[col].append(node.val)
                if node.left:
                    queue.append([node.left, col - 1])
                if node.right:
                    queue.append([node.right, col + 1])
        result = []
        key = sorted(list(res.keys()))
        for k in key:
            result.append(res[k])
        return result
    

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