from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        while i < len(nums):
            if i == len(nums) - 1:
                return nums[i]
            elif nums[i] == nums[i + 1]:
                i += 2
            else:
                return nums[i]