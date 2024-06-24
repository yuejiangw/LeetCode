from typing import List
from collections import deque

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m, n = len(maze), len(maze[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = [[False for _ in range(n)] for _ in range(m)]
        queue = deque()

        queue.append(start)
        visited[start[0]][start[1]] = True

        while queue:
            x, y = queue.popleft()
            for dx, dy in dirs:
                nx, ny = x, y
                # 一直走到墙
                while 0 <= nx < m and 0 <= ny < n and maze[nx][ny] == 0:
                    nx += dx
                    ny += dy
                # 把多走的一步回退
                nx -= dx
                ny -= dy
                # 判断是否到达终点
                if nx == destination[0] and ny == destination[1]:
                    return True
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append([nx, ny])
        
        return False
