class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        '''
        可以转化为求最长回文子序列，假设 s 的长度为 n，s 的最长回文子序列为 LPS，那么通过删除 n - LPS 个字符可以得到回文字符串
        则只需要判断 n - LPS 是否 <= k 即可
        '''
        # dp[i][j] 表示 s[i:j] 中的最长回文子序列长度
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        # 初始化 dp[i][i] = 1 代表单独字符本身就是回文
        for i in range(n):
            dp[i][i] = 1
        # 状态转移
        for length in range(2, n + 1):  # 子串长度从 2 开始
            for i in range(n - length + 1): # i 代表子串的起点，取值范围是 0 ~ [n - length]
                j = i + length - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                elif s[i] != s[j]:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]) 

        lps_length = dp[0][n - 1]
        return n - lps_length <= k