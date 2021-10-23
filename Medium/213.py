from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_range(nums):
            if len(nums) == 1:
                return nums[0]
            if len(nums) == 2:
                return max(nums)
            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
            return dp[-1]

        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        # 成环以后首尾房间不能同时偷，因此有两种情况，一是不考虑首位元素，二是不考虑末尾元素
        # 取二者最大
        return max(rob_range(nums[1:]), rob_range(nums[:-1]))