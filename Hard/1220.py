class Solution:
    def countVowelPermutation(self, n: int) -> int:
        """
        dp[i][0]: 第 i 位字符是 a 的可能情况数量
        dp[i][1]: 第 i 位字符是 e 的可能情况数量
        dp[i][2]: 第 i 位字符是 i 的可能情况数量
        dp[i][3]: 第 i 位字符是 o 的可能情况数量
        dp[i][4]: 第 i 位字符是 u 的可能情况数量
        """
        dp = [[0] * 5 for _ in range(n + 1)]
        for j in range(5):
            dp[1][j] = 1

        for i in range(2, n + 1):
            # a 的前一个字符可能是 e, i, u
            dp[i][0] = dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][4]
            # e 的前一个字符可能是 a, i
            dp[i][1] = dp[i - 1][0] + dp[i - 1][2]
            # i 的前一个字符可能是 e, o
            dp[i][2] = dp[i - 1][1] + dp[i - 1][3]
            # o 的前一个字符可能是 i
            dp[i][3] = dp[i - 1][2]
            # u 的前一个字符可能是 o, i
            dp[i][4] = dp[i - 1][2] + dp[i - 1][3]
        return sum(dp[n]) % (10 ** 9 + 7)
