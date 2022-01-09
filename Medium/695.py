from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        res = 0

        def dfs(x, y):
            if x < 0 or x >= row or y < 0 or y >= col:
                return 0
            if grid[x][y] == 0:
                return 0
            grid[x][y] = 0
            return dfs(x - 1, y) + dfs(x + 1, y) + dfs(x, y - 1) + dfs(x, y + 1) + 1
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    res = max(res, dfs(i, j))
        return res