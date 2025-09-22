from typing import List
from collections import defaultdict

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        group = defaultdict(list)
        visited = [False] * n

        def dfs(start, id):
            visited[start] = True
            group[id].append(start)
            for adj in graph[start]:
                if not visited[adj]:
                    dfs(adj, id)
        
        id = 0
        for i in range(n):
            if not visited[i]:
                dfs(i, id)
                id += 1
        
        # 所有节点对数 = n * (n - 1) // 2
        # 连通分量内部节点对数 = size * (size - 1) // 2
        # 所有节点对数 - 所有连通分量内部节点对数就是结果
        total = n * (n - 1) // 2
        reachable = sum([len(v) * (len(v) - 1) // 2 for v in group.values()])
        return total - reachable
