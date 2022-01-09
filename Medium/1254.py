from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        
        def dfs(x, y):
            """ 从 x, y 开始，将相邻的陆地都变成海水 """
            if x < 0 or x >= row or y < 0 or y >= col:
                return
            if grid[x][y] == 1:
                return
            grid[x][y] = 1
            dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            for dx, dy in dirs:
                dfs(x + dx, y + dy)
        
        
        for j in range(col):
            # 将矩形上沿的岛屿全变成水
            dfs(0, j)
            # 将矩形下沿的岛屿全变成水
            dfs(row - 1, j)
        for i in range(row):
            # 将矩形左沿的岛屿全变成水
            dfs(i, 0)
            # 将矩形右沿的岛屿全变成水
            dfs(i, col - 1)
        
        res = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    res += 1
                    dfs(i, j)
        return res