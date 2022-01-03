from collections import defaultdict
from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # 将 edge 中的两个端点加入 graph 中
        def add_edge(graph, edge):
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])

        # 根据现有的图，判断能否找到一条从 source 到 target 的路径
        def dfs(graph, source, target, visited):
            if source == target:
                return True
            else:
                visited[source] = True
                for v in graph[source]:
                    if v not in visited and dfs(graph, v, target, visited):
                        return True
            return False

        graph = defaultdict(set)
        for edge in edges:
            if edge[0] not in graph or edge[1] not in graph:
                add_edge(graph, edge)
            else:
                # 如果根据现有的图可以找到一条连接 edge[0] 和 edge[1] 的路径，
                # 则说明 edge 是一条冗余的边，否则说明它不是，将其加入 graph 中
                visited = {}
                if dfs(graph, edge[0], edge[1], visited):
                    return edge
                else:
                    add_edge(graph, edge)
