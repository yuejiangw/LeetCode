from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        res = []
        visited = set()

        def dfs(i):
            if i in visited:
                return False
            visited.add(i)
            for v in graph[i]:
                if not dfs(v):
                    return False
            visited.remove(i)
            graph[i] = []
            return True

        for i in range(len(graph)):
            if dfs(i):
                res.append(i)
        return res
