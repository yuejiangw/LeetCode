from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        # dp[j]表示凑钱数为j所需的硬币数量
        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1

        for i in range(len(coins)):
            for j in range(coins[i], amount + 1):
                dp[j] += dp[j - coins[i]]
        return dp[amount]