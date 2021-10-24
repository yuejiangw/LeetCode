from typing import List

class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        """与最长公共子序列一模一样"""
        l1 = len(nums1) + 1
        l2 = len(nums2) + 1
        dp = [[0 for _ in range(l2)] for _ in range(l1)]

        for i in range(1, l1):
            for j in range(1, l2):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]