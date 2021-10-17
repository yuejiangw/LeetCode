from typing import List

class Solution:
    def coinChange(self, coins, amount):
        memo = dict()
        def dp(n):
            if n in memo:
                return memo[n]
            if n == 0:
                return 0
            if n < 0:
                return -1
            res = float('INF')
            for coin in coins:
                subProblem = dp(n - coin)
                if subProblem == -1:
                    continue
                res = min(res, 1 + subProblem)
            memo[n] = res if res != float('INF') else -1
            return memo[n]
        return dp(amount)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # dp[j]表示凑足总额为j的硬币数量最少为dp[j]
        dp = [float('inf') for _ in range(amount + 1)]
        
        # 初始化，dp[0] = 0，其它元素都为正无穷
        dp[0] = 0

        # 递推公式：对于当前硬币金额coin，要么拿，要么不拿
        # 拿了，则dp[j] = dp[j - coin] + 1
        # 不拿，则dp[j]不变
        # 取二者中较小的一个作为dp[j]
        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] = min(dp[j], dp[j - coin] + 1)
        return -1 if dp[amount] == float('inf') else dp[amount]