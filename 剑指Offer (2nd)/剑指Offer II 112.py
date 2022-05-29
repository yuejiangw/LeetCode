from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        lookup = [[0] * n for _ in range(m)]

        def dfs(i, j):
            if lookup[i][j] != 0:
                return lookup[i][j]
            res = 1
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                    res = max(res, 1 + dfs(x, y))
            lookup[i][j] = res
            return res
        
        return max(dfs(i, j) for i in range(m) for j in range(n))