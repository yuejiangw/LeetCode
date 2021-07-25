class Solution:
    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] == 0:
            return 0
        area = 1
        grid[i][j] = 0
        area += self.dfs(grid, i - 1, j)
        area += self.dfs(grid, i + 1, j)
        area += self.dfs(grid, i, j - 1)
        area += self.dfs(grid, i, j + 1)
        return area

    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                result = max(result, self.dfs(grid, i, j))
        return result