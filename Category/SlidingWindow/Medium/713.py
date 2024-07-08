from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        i, j = 0, 0
        window = 1
        res = 0
        while j < len(nums):
            c = nums[j]
            j += 1
            window *= c
            while i < j and window >= k:
                d = nums[i]
                i += 1
                window //= d
            res += j - i
        return res
