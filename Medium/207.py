from typing import List


class Solution:
    has_cycle = False

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # T: O(m + n)
        # S: O(m + n)
        # m: 边的数量   n: 顶点的数量
        # 邻接表
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[a].append(b)
        
        visited = [False] * numCourses
        on_path = [False] * numCourses

        # 从节点 s 开始遍历 graph 图
        def dfs(graph, s):
            if on_path[s]:
                self.has_cycle = True

            if visited[s] or self.has_cycle:
                return
            visited[s] = True
            on_path[s] = True
            for adj in graph[s]:
                dfs(graph, adj)
            on_path[s] = False
        
        for s in range(numCourses):
            dfs(graph, s)
        return not self.has_cycle
