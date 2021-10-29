class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """最少删除步数"""
        l1 = len(word1) + 1
        l2 = len(word2) + 1

        # dp[i][j]: 下标为i-1的word1与下标为j-1的word2的最短编辑距离为dp[i][j]
        dp = [[0 for _ in range(l2)] for _ in range(l1)]

        for i in range(l1):
            dp[i][0] = i
        for j in range(l2):
            dp[0][j] = j
        
        for i in range(1, l1):
            for j in range(1, l2):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(1 + dp[i- 1][j], 1 + dp[i][j - 1], 2 + dp[i - 1][j - 1])
        return dp[-1][-1]