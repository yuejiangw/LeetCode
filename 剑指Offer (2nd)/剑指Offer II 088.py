from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost) + 1
        dp = [0] * n
        dp[0] = 0
        dp[1] = 0
        i = 2
        while i < n:
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
            i += 1
        return dp[-1]