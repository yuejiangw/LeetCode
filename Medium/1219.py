from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visit = [[False] * n for _ in range(m)]
        res = 0
        path = 0

        def dfs(i, j):
            """ 获取当前金块, 并向四周扩散 """
            nonlocal path, res
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0 or visit[i][j]:
                res = max(res, path)
                return
            visit[i][j] = True  # 因为每个金块只能被开采一次，因此用visited数组来记录
            path += grid[i][j]
            for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:   # 向四周扩散开采
                x, y = i + dx, j + dy
                dfs(x, y)
            path -= grid[i][j]  # 扩散结束之后回溯
            visit[i][j] = False

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    dfs(i, j)
        return res
