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