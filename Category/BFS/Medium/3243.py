from collections import deque
from typing import List

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        def bfs(graph):
            stack = deque([0])
            dist = [-1] * n
            dist[0] = 0
            while stack:
                l = len(stack)
                for _ in range(l):
                    node = stack.popleft()
                    if node == n - 1:
                        return dist[n-1]
                    for adj in graph[node]:
                        if dist[adj] == -1:
                            dist[adj] = dist[node] + 1
                            stack.append(adj)
            return dist[n-1]
        
        graph = [[] for _ in range(n)]
        for i in range(n - 1):
            graph[i].append(i + 1)
        
        res = []
        for a, b in queries:
            graph[a].append(b)
            res.append(bfs(graph))
        
        return res

