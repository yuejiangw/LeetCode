class Solution:
    # 中心扩散
    # 时间复杂度 O(n^2)
    # 空间复杂度 O(1)
    def countSubstrings(self, s: str) -> int:
        def spread(left, right):
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count

        result = 0
        # 分别考虑回文串长度为奇数和偶数的情况
        for i in range(len(s)):
            result += spread(i, i)

        for i in range(len(s) - 1):
            result += spread(i, i + 1)
        return result

class Solution:
    def countSubstrings(self, s: str) -> int:
        """动态规划"""
        
        l = len(s)
        
        # dp[i][j] 代表下标从i到j的s的回文串个数
        dp = [[False for _ in range(l)] for _ in range(l)]

        res = 0
        for i in range(l - 1, -1, -1):
            for j in range(i, l):
                if s[i] == s[j]:
                    if j - i <= 1:
                        res += 1
                        dp[i][j] = True
                    elif dp[i + 1][j - 1]:
                        dp[i][j] = True
                        res += 1
        return res
