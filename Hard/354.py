from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes = sorted(envelopes, key=lambda x: (x[0], -x[1]))
        max_num = 1
        dp = [1] * len(envelopes)
        for i in range(1, len(envelopes)):
            for j in range(i):
                if envelopes[i][1] > envelopes[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
            max_num = max(max_num, dp[i])
        return max_num
