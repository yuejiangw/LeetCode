from collections import defaultdict
from typing import List


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # 本质上仍为二分图判定，节点为1-n，根据 dislikes 建立连通关系，需要注意的是该图
        # 为无向图，因此建立邻接表时两个节点都要插入对方的值。之后基于 DFS 对二分图进行涂色即可。
        # T: O(n + m)
        # S: O(n)
        # n 为节点数量，m 为边的数量
        self.res = True
        graph = defaultdict(list)
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = [False] * (n + 1)
        color = [False] * (n + 1)

        def dfs(s):
            if not self.res:
                return
            visited[s] = True
            for adj in graph[s]:
                if not visited[adj]:
                    color[adj] = not color[s]
                    dfs(adj)
                else:
                    if color[adj] == color[s]:
                        self.res = False
        
        for i in range(1, n + 1):
            if not visited[i] and self.res:
                dfs(i)
        return self.res
