from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # T: O(V + E)
        # S: O(V + E)
        n = len(graph)
        res = []
        path = []
        visited = [False] * n

        def dfs(start):
            if start == n - 1:
                res.append(path[:] + [n - 1])
                return

            visited[start] = True
            path.append(start)
            for node in graph[start]:
                if not visited[node]:
                    dfs(node)
            path.pop()
            visited[start] = False
        
        dfs(0)
        return res
