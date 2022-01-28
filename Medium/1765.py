from typing import List
from collections import deque

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        # 多源bfs，从水域出发进行 bfs，每向外扩散一层则高度 + 1
        m, n = len(isWater), len(isWater[0])
        res = [[float('-inf')] * n for _ in range(m)]

        # 初始化，将所有水域坐标加入队列，并且将其高度置为 1
        queue = deque()
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    queue.append((i, j, 0))
                    res[i][j] = 0
        while queue:
            length = len(queue)
            for _ in range(length):
                i, j, level = queue.popleft()
                for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if 0 <= x < m and 0 <= y < n and res[x][y] == float('-inf'):
                        res[x][y] = level + 1
                        queue.append((x, y, level + 1))
        return res
