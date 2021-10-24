class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1 = len(text1) + 1
        l2 = len(text2) + 1

        # ⻓度为[0, i - 1]的字符串text1与⻓度为[0, j - 1]的字符串text2的最⻓公共⼦序列为dp[i][j]
        dp = [[0 for _ in range(l2)] for _ in range(l1)]

        # 最长子序列不要求连续，有两种可能
        # text1[i - 1] 与 text2[j - 1]相同，text1[i - 1] 与 text2[j - 1]不相同
        # 如果 text1[i - 1] 与 text2[j - 1]相同，那么dp[i][j] = dp[i - 1][j - 1] + 1
        # 如果 text1[i - 1] 与 text2[j - 1]不相同，那就看看 text1[0, i - 2]与 text2[0, j - 1]
        # 的最⻓公共⼦序列，和 text1[0, i - 1] 与 text2[0, j - 1] 的最⻓公共⼦序列，取最⼤的
        for i in range(1, l1):
            for j in range(1, l2):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[-1][-1]