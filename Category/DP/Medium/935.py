class Solution:
    def knightDialer(self, n: int) -> int:
        """
        1. 把数字分成4类: 1379，46，28和0，分别为A，B，C，D
        2. 1379可以由46和28得到，且46和28中的每个数字都可以到达1379中的两个，
           所以 A = (B + C) * 2
        3. 46可以由1379和0得到，其中1379可以到达46中的一个，0可以到达46中的每一个，
           所以 B = A + D * 2
        4. 28可以由1379得到，其中1379可以到达28中的一个，所以 C = A
        5. 0可以由46得到，其中46可以到达0，所以 D = B
        6. 递推即可得到最终答案
        """
        if n == 1:
            return 10

        # states 代表 A, B, C, D 中的数字个数
        states = [4, 2, 2, 1]
        for _ in range(n - 1):
            states = [
                (states[1] + states[2]) * 2, states[0] + states[3] * 2, states[0], states[1]]
        return sum(states) % (10**9 + 7)

class Solution:
    def knightDialer(self, n: int) -> int:
        dp = [[0] * 10 for _ in range(n)]
        dp[0] = [1] * 10
        for i in range(1, n):
            dp[i][0] = dp[i - 1][4] + dp[i - 1][6]
            dp[i][1] = dp[i - 1][6] + dp[i - 1][8]
            dp[i][2] = dp[i - 1][7] + dp[i - 1][9]
            dp[i][3] = dp[i - 1][4] + dp[i - 1][8]
            dp[i][4] = dp[i - 1][3] + dp[i - 1][9] + dp[i - 1][0]
            dp[i][6] = dp[i - 1][7] + dp[i - 1][1] + dp[i - 1][0]
            dp[i][7] = dp[i - 1][2] + dp[i - 1][6]
            dp[i][8] = dp[i - 1][1] + dp[i - 1][3]
            dp[i][9] = dp[i - 1][2] + dp[i - 1][4]
            dp[i][0] = dp[i - 1][4] + dp[i - 1][6]
        return sum(dp[-1]) % 1000000007