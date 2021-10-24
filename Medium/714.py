from typing import List
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if len(prices) <= 1:
            return 0
        
        # dp[i][0] 代表买入状态，dp[i][1]代表卖出状态
        dp = [[0, 0] for _ in range(len(prices))]
        dp[0][0] = -prices[0]

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i] - fee)
        return max(dp[-1])