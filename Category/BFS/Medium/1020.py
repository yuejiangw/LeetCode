from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        row = len(grid)
        col = len(grid[0])

        def dfs(i, j):
            if i < 0 or j < 0 or i >= row or j >= col:
                return
            if grid[i][j] == 0:
                return
            grid[i][j] = 0
            for dx, dy in dirs:
                x = i + dx
                y = j + dy
                dfs(x, y)

        for i in range(row):
            dfs(i, 0)
            dfs(i, col - 1)
        for j in range(col):
            dfs(0, j)
            dfs(row - 1, j)

        res = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    res += 1
        return res


from collections import deque
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        row = len(grid)
        col = len(grid[0])

        def bfs(i, j):
            visited = [[0] * col for _ in range(row)]
            queue = deque([(i, j)])
            visited[i][j] = 1
            while queue:
                length = len(queue)
                for _ in range(length):
                    x, y = queue.popleft()
                    grid[x][y] = 0
                    for dx, dy in dirs:
                        x_next = x + dx
                        y_next = y + dy
                        if 0 <= x_next < row and 0 <= y_next < col and not visited[x_next][y_next] \
                                and grid[x_next][y_next]:
                            queue.append((x_next, y_next))
                            visited[x_next][y_next] = 1

        for i in range(row):
            if grid[i][0] == 1:
                bfs(i, 0)
            if grid[i][col - 1] == 1:
                bfs(i, col - 1)
        for j in range(col):
            if grid[0][j] == 1:
                bfs(0, j)
            if grid[row - 1][j] == 1:
                bfs(row - 1, j)

        res = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    res += 1
        return res
