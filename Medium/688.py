class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        """ 记忆化搜索 """
        memo = {}   # memo 装的是概率
        def dfs(i, j, count):
            """ 在起始位置为 (i, j), 最多走 count 的情况下, 停止在棋盘内的概率 """
            if i < 0 or j < 0 or i >= n or j >= n:
                return 0
            if count == k:
                return 1
            if (i, j, count) in memo:
                return memo[(i, j, count)]
            
            p = 0   # 累加各个方向的概率
            # 8个方向
            for x, y in [(i-1, j+2), (i-2, j+1), (i-1, j-2), (i-2, j-1),
                    (i+1, j+2), (i+2, j+1), (i+1, j-2), (i+2, j-1)]:
                p += dfs(x, y, count + 1)
            p /= 8
            memo[(i, j, count)] = p
            return p

        return dfs(row, column, 0)