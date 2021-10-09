from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        dp = [[0 for _ in range(col)] for _ in range(row)]
        
        # initialize
        i = 0
        while i < row and obstacleGrid[i][0] == 0:
            dp[i][0] = 1
            i += 1
        j = 0
        while j < col and obstacleGrid[0][j] == 0:
            dp[0][j] = 1
            j += 1

        # dynamic programming
        for i in range(1, row):
            for j in range(1, col):
                if obstacleGrid[i][j] == 1:
                    continue
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]