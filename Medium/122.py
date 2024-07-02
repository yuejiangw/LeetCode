from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Greedy，尽可能找低价买入，只要当前股价比买入价高就卖出，尽可能多频次地交易
        res = 0
        curr_val = prices[0]
        for i in range(1, len(prices)):
            # 找到了更便宜的买入价
            if prices[i] <= curr_val:
                curr_val = prices[i]
            else:
                # 卖出股票
                res += prices[i] - curr_val
                curr_val = prices[i]
        return res

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        # dp[i][0] 代表第i天持有股票的最大钱数
        # dp[i][1] 代表第i天不持有股票的最大钱数
        dp = [[0, 0] for _ in range(len(prices))]
        dp[0][0] = -prices[0]
        dp[0][1] = 0

        for i in range(1, len(prices)):
            # 第i天持有股票有两种情况：第i-1天也持有股票，或者第i-1天不持有股票，第i天买入
            # 本题中可以多次买卖，所以第二种情况用dp[i - 1][1] + prices[i]
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])
        return max(dp[-1])


class Solution:
    """贪心，找所有正区间"""
    def maxProfit(self, prices: List[int]) -> int:
        greedy = [0 for _ in range(len(prices))]
        greedy[0] = -prices[0]
        res = 0
        for i in range(1, len(prices)):
            greedy[i] = prices[i] - prices[i - 1]
            if greedy[i] > 0:
                res += greedy[i]
        return res
