from typing import List
from collections import defaultdict


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        n = len(adj)
        total = sum(range(1, n + 1))
        return [k for k in adj.keys() if sum(adj[k]) == total - k][0]