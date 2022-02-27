from typing import List
from collections import deque


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        # BFS, 从门出发, 依次填充各个相邻的空房间
        m, n = len(rooms), len(rooms[0])
        queue = deque()
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append([i, j, 0])

        while queue:
            length = len(queue)
            for _ in range(length):
                a, b, step = queue.popleft()
                for x, y in [(a-1, b), (a+1, b), (a, b-1), (a, b+1)]:
                    if 0 <= x < m and 0 <= y < n and rooms[x][y] == 2147483647:
                        rooms[x][y] = step + 1
                        queue.append([x, y, step + 1])
        
