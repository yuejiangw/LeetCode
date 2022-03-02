from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        # T: O(N)
        # S: O(1)
        is_increase = False
        is_decrease = False
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                is_increase = True
            elif nums[i] > nums[i + 1]:
                is_decrease = True
        return not (is_increase and is_decrease)