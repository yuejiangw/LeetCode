class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        """ 记忆化搜索 """
        memo = {}
        def dfs(i, j, count):
            if i < 0 or j < 0 or i >= n or j >= n:
                return 0
            if count == k:
                return 1
            if (i, j, count) in memo:
                return memo[(i, j, count)]
            
            p = 0
            for x, y in [(i-1, j+2), (i-2, j+1), (i-1, j-2), (i-2, j-1),
                    (i+1, j+2), (i+2, j+1), (i+1, j-2), (i+2, j-1)]:
                p += dfs(x, y, count + 1)
            p /= 8
            memo[(i, j, count)] = p
            return p

        return dfs(row, column, 0)