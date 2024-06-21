from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        curr_min = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] < curr_min:
                curr_min = prices[i]
            else:
                profit = prices[i] - curr_min
                max_profit = max(profit, max_profit)
        return max_profit 


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """贪心算法，在左区间取最小值，右区间取最大值"""
        low = float('inf')
        res = 0
        for i in range(len(prices)):
            low = min(low, prices[i])
            res = max(res, prices[i] - low)
        return res
    
    def maxProfit(self, prices: List[int]) -> int:
        """动态规划"""
        if len(prices) == 1:
            return 0
        # dp[i][0]表示第i天持有股票所得的最多现金
        # dp[i][1]表示第i天不持有股票所得的最多现金
        dp = [[0, 0] for _ in range(len(prices))]
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        for i in range(1, len(prices)):
            # 如果第i天持有股票则有两种情况：第i-1天也持有股票，或第i天买入股票
            # 此题规定只能1次买卖，所以第i天买入股票的最大价值为-prices[i]，不是
            # max(prices[i - 1]) - prices[i]
            dp[i][0] = max(dp[i - 1][0], -prices[i])

            # 如果第i天不持有股票则也有两种情况：第i-1天也不持有股票，或第i天卖出股票
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])
        return max(dp[-1])
