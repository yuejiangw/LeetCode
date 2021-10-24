from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        # dp数组，每行有四个状态，以dp[i][j]举例，j = [0, 1, 2, 3]
        # j = 0: 当前为买入股票状态
        # j = 1: 两天前卖出了股票，持续至今，当前为卖出状态
        # j = 2: 今天刚刚卖出了股票，当前为卖出状态
        # j = 3: 今天为冷冻状态，持续一天
        dp = [[0 for _ in range(4)] for _ in range(len(prices))]

        dp[0][0] = -prices[0]
        
        for i in range(1, len(prices)):
            # 今天为买入状态，一共有两种可能：一是前一天也为买入状态，此时为dp[i - 1][0]
            # 二是前一天为冷冻状态或卖出状态，今天买入，取二者中较大者。对于卖出状态，由于
            # 卖出后紧接着的第二天要冷冻，因此这里取dp[i - 1][1]，而不是dp[i - 1][2]
            dp[i][0] = max(dp[i - 1][0], max(dp[i - 1][3], dp[i - 1][1]) - prices[i])
            
            # 若今天持续卖出状态，则昨天可能也为持续卖出状态，或者为冷冻状态，今天解冻
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][3])
            
            # 若当前为卖出状态，则昨天一定是买入股票状态
            dp[i][2] = dp[i - 1][0] + prices[i]

            # 若当前为冷冻状态，则昨天一定是卖出状态
            dp[i][3] = dp[i - 1][2]
            
        return max(dp[-1])