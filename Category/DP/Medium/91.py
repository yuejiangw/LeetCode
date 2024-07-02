class Solution:
    def numDecodings(self, s: str) -> int:
        """
        动态规划, 时间复杂度 O(N), 空间复杂度 O(N), 可以优化为 O(1) 的空间复杂度
        """
        n = len(s)
        # dp[i]: s 中的前 i 个字符一共有 dp[i] 种解码方法
        dp = [0] * (n + 1)
        # 初始化, 空字符串有一种解码方法
        dp[0] = 1
        for i in range(1, n + 1):
            # 使用一个字符进行解码: 如果 s 中当前字符不为0, 则可以解码
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]
            # 使用两个字符进行解码: 如果 s 中前一个字符不为0, 且两个字符连在一起组成的整数不大于26, 则可以解码
            if i > 1 and s[i - 2] != '0' and 0 < int(s[i - 2: i]) <= 26:
                dp[i] += dp[i - 2]
        return dp[n]


    def numDecodings(self, s: str) -> int:
        """
        动态规划优化版本, 时间复杂度 O(N), 空间复杂度 O(1)
        """
        n = len(s)
        # a = dp[i - 2], b = dp[i - 1], c = dp[i]
        a, b, c = 0, 1, 0
        for i in range(1, n + 1):
            c = 0
            # 使用一个字符进行解码: 如果 s 中当前字符不为0, 则可以解码
            if s[i - 1] != '0':
                c += b
            # 使用两个字符进行解码: 如果 s 中前一个字符不为0, 且两个字符连在一起组成的整数不大于26, 则可以解码
            if i > 1 and s[i - 2] != '0' and 0 < int(s[i - 2: i]) <= 26:
                c += a
            a, b = b, c
        return c