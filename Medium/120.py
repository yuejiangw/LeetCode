from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        1. dp, dp[i][j] represents for the min path sum to reach [i, j]
        2. to reach [i, j], there are two possibilities: from [i-1, j-1], or from [i-1, j]
        3. corner case:
            j = 0, then there is no j - 1, so [i, 0] = [i-1, 0]
            i = j, reach the end of the row, so [i, j] = [i-1, j-1]
        4. T: O(N^2), S: O(N^2)
        5. base: dp[0][0] = triangle[0][0]
        """
        n = len(triangle)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        dp[0][0] = triangle[0][0]
        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] + triangle[i][0]
            for j in range(1, i):
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
            dp[i][i] = dp[i - 1][i - 1] + triangle[i][i]
        return min(dp[-1])