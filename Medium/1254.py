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

from collections import deque
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        def bfs(i, j):
            queue = deque()
            visited = [[0] * col for _ in range(row)]
            queue.append((i, j))
            visited[i][j] = 1
            while queue:
                length = len(queue)
                for _ in range(length):
                    x, y = queue.popleft()
                    if grid[x][y] == 1:
                        continue
                    grid[x][y] = 1
                    visited[x][y] = 1
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        x_next = x + dx
                        y_next = y + dy
                        if x_next < 0 or x_next >= row or y_next < 0 or y_next >= col:
                            continue
                        if visited[x_next][y_next] == 0:
                            queue.append((x_next, y_next))

        for i in range(row):
            bfs(i, 0)
            bfs(i, col - 1)
        for j in range(col):
            bfs(0, j)
            bfs(row - 1, j)

        res = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    bfs(i, j)
                    res += 1
        return res
