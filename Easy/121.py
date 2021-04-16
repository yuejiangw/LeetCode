
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