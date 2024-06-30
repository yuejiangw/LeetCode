from typing import List
from collections import deque


class Solution:
    """ DFS """
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


class Solution:
    """ BFS """
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        row = len(grid)
        col = len(grid[0])

        def is_valid(i, j):
            if i < 0 or i >= row or j < 0 or j >= col or grid[i][j] == 0:
                return False
            return True

        def bfs(x, y):
            queue = deque([(x, y)])
            res = 0
            while queue:
                length = len(queue)
                for _ in range(length):
                    i, j = queue.popleft()
                    if is_valid(i, j):
                        res += 1
                        grid[i][j] = 0
                        for dx, dy in dirs:
                            new_x = i + dx
                            new_y = j + dy
                            queue.append((new_x, new_y))
            return res

        res = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    res = max(res, bfs(i, j))

        return res
