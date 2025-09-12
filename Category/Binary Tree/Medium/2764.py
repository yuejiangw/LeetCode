from typing import List
from collections import defaultdict

class Solution:
    def isPreorder(self, nodes: List[List[int]]) -> bool:
        # nodes = [[0,-1],[1,0],[2,0],[3,1],[4,1]]
        # parent_to_node: {-1: [0], 0: [1, 2], 1: [3, 4]}
        root = 0
        parent_to_node = defaultdict(list)
        for node, parent in nodes:
            parent_to_node[parent].append(node)
            if parent == -1:
                root = node
        
        k = 0
        def dfs(node):
            nonlocal k
            if k >= len(nodes) or node != nodes[k][0]:
                return False
            k += 1
            for child in parent_to_node[node]:
                if not dfs(child):
                    return False
            return True
        
        return dfs(root) and k == len(nodes)
