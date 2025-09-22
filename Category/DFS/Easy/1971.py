from typing import List
from collections import defaultdict

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = [False] * n
        def dfs(start):
            visited[start] = True
            if start == destination:
                return True
            for adj in graph[start]:
                if not visited[adj]:
                    if dfs(adj):
                        return True
            return False
        
        return dfs(source)
