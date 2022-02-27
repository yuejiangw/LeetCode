from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # BFS, 时间复杂度 O(N^2), 空间复杂度 O(N)

        # 所需时间
        res = 0
        # 新鲜橘子数量
        cnt = 0
        m, n = len(grid), len(grid[0])

        queue = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    cnt += 1
    
        while queue and cnt > 0:
            length = len(queue)
            for _ in range(length):
                a, b = queue.popleft()
                for x, y in [(a-1, b), (a+1, b), (a, b-1), (a, b+1)]:
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                        queue.append((x, y))
                        grid[x][y] = 2
                        cnt -= 1
            res += 1
        
        return res if cnt == 0 else -1