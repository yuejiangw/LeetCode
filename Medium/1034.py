from typing import List


class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        visited[row][col] = True
        borders = []

        def dfs(i, j):
            is_border = False
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                x, y = i + dx, j + dy
                if not (0 <= x < m and 0 <= y < n and grid[x][y] == grid[i][j]):
                    is_border = True
                elif not visited[x][y]:
                    visited[x][y] = True
                    dfs(x, y)
            if is_border:
                borders.append((i, j))
        
        dfs(row, col)
        for i, j in borders:
            grid[i][j] = color
        return grid

