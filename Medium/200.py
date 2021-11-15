from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
                return
            grid[i][j] = '2'
            x = [1, 0, -1, 0]
            y = [0, 1, 0, -1]
            for idx in range(4):
                dfs(grid, i + x[idx], j + y[idx])

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    res += 1
        return res
