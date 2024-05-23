from typing import List

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # 记录峰值数量
        if len(nums) <= 1:
            return len(nums)
        pre_diff = 0
        curr_diff = 0
        res = 1
        for i in range(len(nums) - 1):
            curr_diff = nums[i + 1] - nums[i]
            if (curr_diff < 0 and pre_diff >= 0) or (curr_diff > 0 and pre_diff <= 0):
                res += 1
                pre_diff = curr_diff
        return res
