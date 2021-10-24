from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k == 0 or not prices:
            return 0

        # dp[i][j]，当j为奇数时代表买入，j为偶数时代表卖出
        dp = [[0 for _ in range(2 * k + 1)] for _ in range(len(prices))]

        # 初始化，i = 0时所有的买入操作(j为奇数)的值都是-prices[0]
        for j in range(1, 2 * k + 1, 2):
            dp[0][j] = -prices[0]
        
        for i in range(1, len(prices)):
            for j in range(1, 2 * k + 1):
                # j为0代表状态为无任何操作，一直为0，因此跳过
                # j为奇数，代表此时为买入操作，两种可能：要么第i-1天也为相同的状态，
                # 要么第i-1天为卖出股票状态，第i天买入，取二者中较大者
                if j % 2 == 1:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] - prices[i])

                # j为偶数，代表此时为卖出操作，两种可能：要么第i-1天也为相同的状态，
                # 要么第i-1天为买入股票状态，第i天出售，取二者中较大者
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + prices[i])
        
        return max(dp[-1])