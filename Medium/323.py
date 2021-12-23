from typing import List
from collections import defaultdict


class Solution:
    def get_adj(self, edges):
        adj = defaultdict(list)
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        return adj

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n == 1:
            return 1

        adj = self.get_adj(edges)
        vertexes = list(range(n))
        visited = set()
        count = 0

        def dfs(vertex, visited):
            visited.add(vertex)
            for adj_vertex in adj[vertex]:
                if not adj_vertex in visited:
                    dfs(adj_vertex, visited)

        for vertex in vertexes:
            if vertex not in visited:
                dfs(vertex, visited)
                count += 1

        return count
