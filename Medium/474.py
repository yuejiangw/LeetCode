from typing import List

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        def calculate(s):
            zero_num, one_num = 0, 0
            for c in s:
                if c == '0':
                    zero_num += 1
                else:
                    one_num += 1
            return zero_num, one_num

        # dp[i][j] 代表在0的数量为i，1的数量为j的情况下最大子集的数量
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        # 对于一个字符串，有两种选择，装和不装
        # 不装，则dp[i][j]不变，装，则i和j都要相应减去该字符串中0和1的数量，之后子集数+1
        for s in strs:
            zero_num, one_num = calculate(s)
            i = m
            while i >= zero_num:
                j = n
                while j >= one_num:
                    dp[i][j] = max(dp[i][j], dp[i - zero_num][j - one_num] + 1)
                    j -= 1
                i -= 1
        return dp[m][n]