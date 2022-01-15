from typing import List
from collections import deque


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row = len(heights)
        col = len(heights[0])

        p = [[0] * col for _ in range(row)]
        a = [[0] * col for _ in range(row)]

        def bfs(visited, x, y):
            if visited[x][y] == 1:
                return
            queue = deque()
            queue.append((x, y))
            visited[x][y] = 1
            while queue:
                i, j = queue.popleft()
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    new_x, new_y = i + dx, j + dy
                    if 0 <= new_x < row and 0 <= new_y < col and visited[new_x][new_y] == 0 \
                            and heights[new_x][new_y] >= heights[i][j]:
                        queue.append((new_x, new_y))
                        visited[new_x][new_y] = 1

        for i in range(row):
            bfs(p, i, 0)
            bfs(a, i, col - 1)
        for j in range(col):
            bfs(p, 0, j)
            bfs(a, row - 1, j)

        res = []
        for i in range(row):
            for j in range(col):
                if p[i][j] == 1 and a[i][j] == 1:
                    res.append([i, j])
        return res
