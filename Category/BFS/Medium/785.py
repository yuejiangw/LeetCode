from typing import List
from collections import deque


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # 二分图的定义可以转换为用两种颜色对图进行涂色，任意一条边的两个
        # 端点的颜色不能相同
        # T: O(M + N)
        # S: O(M)
        # M 为顶点个数
        
        self.res = True
        visited = [False] * len(graph)
        color = [False] * len(graph)
        
        # 思路: 利用 DFS 进行涂色
        # 对于与 s 相邻的所有节点，如果其还未涂色，则将其涂色
        # 反之则比较其颜色与 s 的颜色是否相同
        def dfs(s):
            if not self.res:
                return
            visited[s] = True
            for adj in graph[s]:
                if not visited[adj]:
                    color[adj] = not color[s]   # 将 adj 涂上与 s 不同的颜色
                    dfs(adj)
                else:
                    if color[adj] == color[s]:
                        self.res = False
        
        for i in range(len(graph)):
            if not visited[i] and self.res:
                dfs(i)

        return self.res
    

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # 基于 bfs 的二分图判定
        n = len(graph)
        visited = [False] * n
        color = [False] * n
        
        def bfs(s):
            queue = deque([s]) # 用 True 和 False 代表两个 group
            while queue:
                node= queue.popleft()
                visited[node] = True
                for adj in graph[node]:
                    if visited[adj]:
                        if color[adj] == color[node]:
                            return False
                    else:
                        queue.append(adj)
                        color[adj] = not color[node]
            return True
        
        for i in range(n):
            if i not in visited and not bfs(i):
                return False
        return True