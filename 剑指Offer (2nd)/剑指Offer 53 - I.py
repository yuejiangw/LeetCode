from typing import List


class Solution:
    def find_left(self, nums, target):
        i, j = 0, len(nums)
        while i < j:
            mid = i + (j - i) // 2
            print(mid)
            if nums[mid] >= target:
                j = mid
            else:
                i = mid + 1
        return i

    def find_right(self, nums, target):
        i, j = 0, len(nums)
        while i < j:
            mid = i + (j - i) // 2
            if nums[mid] <= target:
                i = mid + 1
            else:
                j = mid
        return i - 1

    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        left_bound = self.find_left(nums, target)
        right_bound = self.find_right(nums, target)
        return right_bound - left_bound + 1
