from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        # dp[i][0] 代表第 i 天持有股票状态下的最大利润
        # dp[i][1] 代表第 i 天卖出股票状态下的最大利润
        dp = [[0] * 2 for _ in range(len(prices))]
        dp[0][0] = -prices[0]
        for i in range(1, len(prices)):
            # 由于规定只能一次买卖，因此 dp[i][0] 的情况为：第 i-1 天
            # 也是持有股票的状态，或者第 i 天刚刚进行第一次买入
            dp[i][0] = max(dp[i-1][0], -prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])
        return max(dp[-1])
