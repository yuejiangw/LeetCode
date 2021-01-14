class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [1, 1]
        for i in range(2, n):
            dp.append(dp[i - 1] + dp[i - 2])
        return dp[n -1] + dp[n - 2]