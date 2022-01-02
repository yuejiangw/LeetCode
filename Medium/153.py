from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        i, j = 0, len(nums) - 1
        while i < j:
            mid = i + (j - i) // 2
            if nums[mid] > nums[j]:
                i = mid + 1
            elif nums[mid] < nums[i]:
                j = mid
            else:
                j -= 1
        return nums[i]


class Solution:
    def findMin(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        while i < j:
            mid = i + (j - i) // 2
            if nums[mid] < nums[j]:
                j = mid
            else:
                i = mid + 1
        return nums[i]
