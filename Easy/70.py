class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]

class Solution:
    """ O(1) 空间复杂度 """
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        pre_1, pre_2 = 1, 2
        for i in range(3, n):
            tmp = pre_1
            pre_1 = pre_2
            pre_2 += tmp
        return pre_1 + pre_2