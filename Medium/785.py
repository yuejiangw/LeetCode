from typing import List


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