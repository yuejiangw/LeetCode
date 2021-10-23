from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # dp[i][j]: j = [0, 1, 2, 3, 4]
        # j = 0: 没有交易操作    j = 1: 第一次买入
        # j = 2: 第一次卖出      j = 3: 第二次买入
        # j = 4: 第二次卖出
        # dp[i][j] 表示第i天状态为j时剩余的最大钱数
        dp = [[0 for _ in range(5)] for _ in range(len(prices))]

        dp[0][0] = 0
        dp[0][1] = -prices[0]
        dp[0][2] = 0
        dp[0][3] = -prices[0]
        dp[0][4] = 0

        for i in range(1, len(prices)):
            dp[i][0] = dp[i - 1][0]
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] + prices[i])
            dp[i][3] = max(dp[i - 1][3], dp[i - 1][2] - prices[i])
            dp[i][4] = max(dp[i - 1][4], dp[i - 1][3] + prices[i])
        
        return max(dp[-1])