from typing import List
from collections import deque


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        """
        First use DFS to find the first island, then use BFS to search the min length path
        from the first island to the second island.
        """
        row = len(grid)
        col = len(grid[0])
        source = deque()

        def dfs(i, j):
            if i < 0 or j < 0 or i >= row or j >= col or grid[i][j] == 0:
                return
            source.append((i, j))
            grid[i][j] = 0
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dfs(i + dx, j + dy)

        find = False
        for i in range(row):
            for j in range(col):
                if not find and grid[i][j] == 1:
                    dfs(i, j)
                    find = True

        res = 0
        visited = set(source)
        while source:
            length = len(source)
            for _ in range(length):
                i, j = source.popleft()
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    x_next = i + dx
                    y_next = j + dy
                    if x_next < 0 or y_next < 0 or x_next >= row or y_next >= col \
                            or (x_next, y_next) in visited:
                        continue
                    if grid[x_next][y_next] == 0:
                        source.append((x_next, y_next))
                        visited.add((x_next, y_next))
                    else:
                        return res
            res += 1
        return res
