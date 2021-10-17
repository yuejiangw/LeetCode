class Solution:
    def numSquares(self, n: int) -> int:

        # dp数组代表当目标为i时，需要的最少的perfect square numbers的数量为dp[i]
        dp = [float('inf') for _ in range(n + 1)]
        # 初始化
        dp[0] = 0
        for i in range(n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        return dp[n]
