# 动态规划思想
# 如果一个字符串是回文串，那么去掉其首尾两个字符之后剩余的字符串仍然是一个回文串
# 用P(i, j)表示字符串s从第i个到第j个字母组成的回文串，则状态转移方程为：
# P(i, j) = P(i+1, j-1) and s[i]==s[j]
# 边界条件：
# 当s的长度为1时它是一个回文串，当s的长度为2时如果两个字符相同则是回文串s
# 搞笑的是，LeetCode官方给的Python动态规划解法居然都超出了后台允许的最大测试时间
# 我服，想搞DP还是用Java吧
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n = len(s)

        # 两个边界条件
        if n == 1:
            return s
        if (n == 2) and (s[0] == s[1]):
            return s

        # 动态规划
        dp = [[False] * n for _ in range(n)]
        ans = ""
        # 枚举子串长度
        for l in range(n):
            for i in range(n):
                j = i + l
                if j >= len(s):
                    break
                if l == 0:
                    dp[i][j] = True
                elif l == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
                if dp[i][j] and l + 1 > len(ans):
                    ans = s[i: j + 1]
        return ans