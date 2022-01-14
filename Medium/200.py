from typing import List
from collections import deque


class Solution:
    """ dfs """
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def dfs(i, j):
            # boundary
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return

            # visited the island, or is water
            if grid[i][j] == '0':
                return

            # visited the island, mark it as 'water'    
            grid[i][j] = '0'

            # start seraching four directions
            for dx, dy in dirs:
                dfs(i + dx, j + dy)

        res = 0
        for i in range(row):
            for j in range(col):
                # if find an island, use dfs to search it
                if grid[i][j] == '1':
                    dfs(i, j)
                    res += 1
        return res


class Solution:
    """ bfs """
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def is_valid(i, j):
            if i < 0 or i >= row or j < 0 or j >= col or grid[i][j] == '0':
                return False
            return True

        def bfs(x, y):
            queue = deque([(x, y)])
            while queue:
                length = len(queue)
                for _ in range(length):
                    i, j = queue.popleft()
                    if is_valid(i, j):
                        grid[i][j] = '0'
                        for dx, dy in dirs:
                            new_x = i + dx
                            new_y = j + dy
                            queue.append((new_x, new_y))
        res = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    bfs(i, j)
                    res += 1
        return res
