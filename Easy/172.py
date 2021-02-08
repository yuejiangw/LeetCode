class Solution:
    def trailingZeroes(self, n: int) -> int:
        dp = [1]
        for i in range(1, n + 1):
            dp.append(dp[i - 1] * i)

        count = 0
        result = str(dp[n])
        for i in range(len(result) - 1, -1, -1):
            if result[i] == '0':
                count += 1
            else:
                return count