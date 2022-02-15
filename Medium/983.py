from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * 366
        # init, dp[0] = 0

        day_idx = 0
        for i in range(1, 366):
            if day_idx >= len(days):
                break
            # If today is not a travel day, then the cost should not change.
            if days[day_idx] != i:
                dp[i] = dp[i - 1]
            # If today is a travel day, then use dynamic programming
            else:   
                dp[i] = min(dp[max(0, i - 1)] + costs[0], dp[max(0, i - 7)] + costs[1],
                            dp[max(0, i - 30)] + costs[2])
                day_idx += 1
        return dp[days[-1]]