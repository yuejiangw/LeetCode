class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        # dp[i][j] 代表 word1[0...i] 和 word2[0...j] 之间的编辑距离
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        # init
        # i == 0 时候代表 word1 是空字符串，同理 j == 0 时候代表 word2 是空字符串
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        # state transfer
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        return dp[m][n]