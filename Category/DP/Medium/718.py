from typing import List


# 2023-07-10
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        # dp[i][j] 含义：
        # nums1[:i] 和 nums2[:j] 之间最长的公共子数组的长度为 dp[i][j]
        dp = [[0 for _ in range(n)] for _ in range(m)]

        res = 0
        # 初始化 dp 数组的第一行和第一列
        for i in range(m):
            if nums1[i] == nums2[0]:
                dp[i][0] = 1
                res = 1
        for j in range(n):
            if nums1[0] == nums2[j]:
                dp[0][j] = 1
                res = 1

        for i in range(1, m):
            for j in range(1, n):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    res = max(res, dp[i][j])
        return res


# 2022-02-27
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        l1 = len(nums1)
        l2 = len(nums2)

        # dp[i][j] 代表以下标为 i 结尾的 nums1，和以下标为 j 结尾的 nums2，
        # 最长重复子数组长度为 dp[i][j]
        dp = [[0 for _ in range(l2)] for _ in range(l1)]

        res = 0
        for i in range(l1):
            if nums1[i] == nums2[0]:
                dp[i][0] = 1
                res = 1
        for j in range(l2):
            if nums1[0] == nums2[j]:
                dp[0][j] = 1
                res = 1

        for i in range(1, l1):
            for j in range(1, l2):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    res = max(res, dp[i][j])
        return res
