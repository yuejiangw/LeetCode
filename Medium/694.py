from typing import List


class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        """
        用一个整数 dir 代表方向，序列化 dfs 时遍历 + 回溯的轨迹，再用 set 去重
        """
        m, n = len(grid), len(grid[0])
        res = set()

        def dfs(i: int, j: int, path: List[int], dir: int) -> None:
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return

            path.append(dir)
            grid[i][j] = 0
            # up, down, left, right
            for dx, dy, d in [(-1, 0, 1), (1, 0, 2), (0, -1, 3), (0, 1, 4)]:
                dfs(i + dx, j + dy, path, d)
            path.append(-dir)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    path = []
                    dfs(i, j, path, 666)    # dir 的初始值可以为任意，因为所有的 dfs 都会用这一个值
                    res.add(','.join(map(str, path)))
        return len(res)
