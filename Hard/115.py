class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        l1 = len(s) + 1
        l2 = len(t) + 1
        # dp[i][j]: 以i-1为结尾的s子序列中出现以j-1为结尾的t子序列的个数
        dp = [[0 for _ in range(l2)] for _ in range(l1)]

        for i in range(l1):
            dp[i][0] = 1
        for j in range(l2):
            dp[0][j] = 0
        dp[0][0] = 1
        for i in range(1, l1):
            for j in range(1, l2):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]