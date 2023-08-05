from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        """
        转换思路，相当于求和等于 sum(nums) - x 的最长子数组的长度，然后
        用 len(nums) 减去这个长度即可
        """
        n = len(nums)
        res = -1
        i, j = 0, 0
        sub_sum = 0
        target = sum(nums) - x
        while j < n:
            sub_sum += nums[j]
            j += 1
            while i < j and sub_sum > target:
                sub_sum -= nums[i]
                i += 1
            if sub_sum == target:
                res = max(res, j - i)
        return n - res if res >= 0 else -1
