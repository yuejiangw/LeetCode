from typing import List
from collections import deque, defaultdict


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


class Solution:
    # 拓扑排序版本
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prerequisite_graph = defaultdict(set)
        dependent_graph = defaultdict(list)
        for a, b in prerequisites:
            prerequisite_graph[a].add(b)
            dependent_graph[b].append(a)
        
        queue = deque([])
        finished = set()
        for i in range(numCourses):
            if len(prerequisite_graph[i]) == 0:
                queue.append(i)
                finished.add(i)
        
        while queue:
            l = len(queue)
            for _ in range(l):
                course = queue.popleft()
                for dependent in dependent_graph[course]:
                    prerequisite_graph[dependent].remove(course)
                    if len(prerequisite_graph[dependent]) == 0:
                        queue.append(dependent)
                        finished.add(dependent)

        return len(finished) == numCourses
        
