from typing import List
class Solution:
    def pondSizes(self, land: List[List[int]]) -> List[int]:
        # T: O(mn)
        # S: O(mn)
        m, n = len(land), len(land[0])
        res = []

        def dfs(i, j):
            res = 1
            land[i][j] = -1
            for x, y in [(i-1, j), (i+1, j), (i, j-1), 
                (i, j+1), (i-1, j-1), (i+1, j-1), (i-1, j+1), (i+1, j+1)]:
                if 0 <= x < m and 0 <= y < n and land[x][y] == 0:
                    res += dfs(x, y)
            return res
        
        for i in range(m):
            for j in range(n):
                if land[i][j] == 0:
                    res.append(dfs(i, j))
        return sorted(res)
