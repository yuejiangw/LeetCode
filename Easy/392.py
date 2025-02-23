class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)

class Solution:
    """ 动态规划，最长子序列是否等于s的长度 """
    def isSubsequence(self, s: str, t: str) -> bool:
        l1 = len(s) + 1
        l2 = len(t) + 1
        dp = [[0 for _ in range(l2)] for _ in range(l1)]

        for i in range(1, l1):
            for j in range(1, l2):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[-1][-1] == len(s)