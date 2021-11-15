from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        fast = 1
        while fast < len(nums):
            if nums[slow] == 0:
                if nums[fast] != 0:
                    nums[slow], nums[fast] = nums[fast], nums[slow]
                    slow += 1
                    fast += 1
                else:
                    fast += 1
            else:
                slow += 1
                fast += 1


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
        while j < len(nums):
            nums[j] = 0
            j += 1
