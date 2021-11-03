from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = nums[i] + max(nums[i - 1], 0)
        return max(nums)


class Solution:
    """动态规划"""
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            if dp[i] > res:
                res = dp[i]
        return res


class Solution:
    """贪心"""
    def maxSubArray(self, nums: List[int]) -> int:
        res = float('-inf')
        count = 0
        for i in range(len(nums)):
            count += nums[i]
            if count > res:
                res = count
            if count <= 0:
                count = 0
        return res
