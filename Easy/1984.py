from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # sliding window
        nums = sorted(nums)
        i, j = 0, 0
        res = float('inf')
        while j < len(nums):
            c = nums[j]
            j += 1
            if j - i == k:
                d = nums[i]
                i += 1
                res = min(res, c - d)
        return res
