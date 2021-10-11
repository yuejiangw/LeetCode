class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[2] = 1
        for i in range(3, n + 1):
            for j in range(1, i):
                # 当 j 固定时，dp[i] = max(j * (i - j), j * dp[i - j])
                # 需要从 1 到 i - 1 遍历 j 之后才可以取dp[i]
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
        return dp[n]