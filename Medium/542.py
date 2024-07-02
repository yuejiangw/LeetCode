from collections import deque
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        res = [[-1 for _ in range(n)] for _ in range(m)]
        queue = deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    res[i][j] = 0
        
        while queue:
            a, b = queue.popleft()
            for x, y in [(a-1, b), (a+1, b), (a, b-1), (a, b+1)]:
                if 0 <= x < m and 0 <= y < n and res[x][y] == -1:
                    queue.append((x, y))
                    res[x][y] = res[a][b] + 1
        
        return res