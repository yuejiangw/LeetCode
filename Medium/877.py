from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        # dp[i][j][0] 代表从 piles[i...j] 这堆石头中先手拿可以得到的最高分
        # dp[i][j][1] 代表从 piles[i...j] 这堆石头中后手拿可以得到的最高分
        dp = [[[0, 0] for _ in range(n)] for _ in range(n)]
        
        # init
        for i in range(n):
            # dp[i][j] 代表从 piles[i...i] 这堆石头中取，由于石头只剩一个了，谁先手谁就得分
            dp[i][i][0] = piles[i]
            dp[i][i][1] = 0
        
        # state transfer, 倒着遍历, 由状态转移方程决定
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                # left 代表如果在 piles[i...j] 先手选择了，选 piles[i] 的最大分数
                # right 代表如果在 piles[i...j] 先手选择了，选 piles[j] 的最大分数
                # 选了 piles[i] 则剩余石头就是 piles[i+1...j]，选了 piles[j] 则剩余石头就是 piles[i][j-1]
                # 不管选哪边，之后的石头堆选择中都是后手，后续可以获得的分数是 dp[i+1][j][1] 或 dp[i][j-1][1]
                left = piles[i] + dp[i+1][j][1]
                right = piles[j] + dp[i][j-1][1]
                if left > right:
                    # 先手选左边
                    dp[i][j][0] = left
                    # 如果对方先手选择了 piles[i]，则留下的是 piles[i+1...j]，此时我变成了先手
                    # 因此 dp[i][j][1] = dp[i+1][j][0]
                    dp[i][j][1] = dp[i+1][j][0]
                else:
                    # 先手选右边
                    dp[i][j][0] = right
                    # 如果对方先手选择了 piles[j]，则留下的是 piles[i...j-1]，此时我变成了先手
                    # 因此 dp[i][j][1] = dp[i][j-1][0]
                    dp[i][j][1] = dp[i][j-1][0]
        
        # 代表 piles[0...n-1] 的比赛结果
        res = dp[0][n - 1]
        return res[0] > res[1]

