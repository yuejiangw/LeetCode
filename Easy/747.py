from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        """
        1. get max num
        2. compare max_num with 2 * nums[i]
        """
        max_num = max(nums)
        for num in nums:
            if num == max_num:
                continue
            else:
                if max_num < 2 * num:
                    return -1
        return nums.index(max_num)
