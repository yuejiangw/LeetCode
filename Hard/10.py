class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not s or not p:
            return False

        m = len(s)
        n = len(p)

        # dp[i][j] 代表 s 的前 i 个字符是否与 p 的前 j 个字符匹配
        dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]

        # base case
        dp[0][0] = True
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # s 和 p 的最后一个字符相同，或者 p 的最后一个字符为 '.'
                # 代表 s 和 p 的最后一个字符已经匹配，继续检查前面的字符
                if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                # 如果 p 的最后一个字符为 '*'，则需要检查 '*' 前面的一个字符：
                # (1) 该字符与 s 的最后一个字符不同，则 '*' 代表删除该字符，继续比较剩余字符
                # (2) 该字符与 s 的最后一个字符相同，或者该字符为 '.' 时，三种可能：
                #   (2.1) p 的末尾两个字符相当于不存在，dp[i][j] = dp[i][j-2]
                #   (2.2) p 的末尾两个字符刚好匹配 s 末尾的字符，dp[i][j] = dp[i-1][j-2]
                #   (2.3) p 的末尾两个字符可能匹配 s 末尾多个相同的连续字符，
                #         则逐个向前查看：dp[i][j] = dp[i-1][j]
                elif p[j - 1] == '*':
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        dp[i][j] = dp[i - 1][j - 2] or dp[i - 1][j] or dp[i][j - 2]
                    else:
                        dp[i][j] = dp[i][j - 2]
        return dp[m][n]
