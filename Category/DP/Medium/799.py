class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # dp[i][j] 代表第 i 行第 j 列所经过的水流量，而不是最终剩余的水量
        dp = [[0 for _ in range(query_row + 2)] for _ in range(query_row + 2)]
        dp[0][0] = poured
        for i in range(query_row + 1):
            for j in range(i + 1):
                # 递推公式：如果水流量小于等于 1 则不会向下流
                # 否则会流向 dp[i + 1][j] 和 dp[i + 1][j + 1]
                if dp[i][j] <= 1:
                    continue
                dp[i + 1][j] += (dp[i][j] - 1) / 2 
                dp[i + 1][j + 1] += (dp[i][j] - 1) / 2 
        return min(dp[query_row][query_glass], 1)