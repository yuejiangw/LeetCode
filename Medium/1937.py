from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        """动态规划
        dp[i][j] 代表选择 points[i][j] 后的最大得分
        状态转移方程为 dp[i][j] = 
            max(dp[i][j], dp[i-1][j'] + abs(j'-j) + points[i][j])
        这里的 j' 的范围为 1~n, 这样做的时间复杂度为 O(mn^2)
        为了降低时间复杂度, 我们可以分类讨论 j' 与 j 的大小关系
        (1) 当 j' < j 时, abs(j'-j) = j - j'
            则原方程变为:
                max(dp[i][j], dp[i-1][j'] + j - j' + points[i][j])
            合并常数项可得:
                max(dp[i][j], (dp[i-1][j'] - j') + points[i][j]+j)
        (2) 当 j' > j 时, abs(j'-j) = j' - j
            则原方程变为:
                max(dp[i][j], dp[i-1][j'] + j' - j) + points[i][j]
            合并常数项可得:
                max(dp[i][j], (dp[i-1][j'] + j') + points[i][j]-j)
        因此可以用两个 for 循环解决嵌套的三层循环, 将时间复杂度降为 O(mn)
        """
        m, n = len(points), len(points[0])

        # dp[i][j] 代表选择 points[i][j] 后的最大得分
        dp = [[0] * n for _ in range(m)]
        for j in range(n):
            dp[0][j] = points[0][j]

        # 状态转移方程
        for i in range(1, m):
            # 动态记录第 i-1 行在 j 左右两侧的最大收益
            left_max = float('-inf')
            for j in range(n):
                # 由 j 的左侧转移过来
                left_max = max(left_max, dp[i-1][j] + j)
                dp[i][j] = max(dp[i][j], 
                               points[i][j] + left_max - j)
            right_max = float('-inf')
            for j in range(n - 1, -1, -1):
                # 由 j 的右侧转移过来
                right_max = max(right_max, dp[i-1][j] - j)
                dp[i][j] = max(dp[i][j],
                               points[i][j] + right_max + j)
        
        res = 0
        for j in range(n):
            res = max(res, dp[m-1][j])
        return res
