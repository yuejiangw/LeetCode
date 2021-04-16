class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        profit = 0
        for i in range(len(prices)-1):
            tmp = prices[i+1] - prices[i]
            if tmp > 0:
                profit += tmp
        return profit
