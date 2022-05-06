from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # T: O(mn)
        # S: O(mn)
        m, n = len(grid), len(grid[0])
        res = 0

        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n:
                return 0
            if grid[i][j] == 0:
                return 0
            tmp = 1
            grid[i][j] = 0
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                tmp += dfs(x, y)
            return tmp
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(res, dfs(i, j))
        return res