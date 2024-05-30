from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        # 先确定右边比左边大的情况，再确定左边比右边大的情况
        dp = [1] * len(ratings)
        # 从前向后
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                dp[i] = dp[i - 1] + 1
        # 从后向前
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                dp[i] = max(dp[i], dp[i + 1] + 1)
        return sum(dp)