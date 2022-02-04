from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """
        T: O(n!)
        S: O(n)
        """
        res = []
        path = [0]

        def backtracking(graph, start):
            n = len(graph)
            if start == n - 1:
                res.append(path[:])
                return
            for i in graph[start]:
                path.append(i)
                backtracking(graph, i)
                path.pop()
        backtracking(graph, 0)
        
        return res
