from collections import defaultdict
from typing import List

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l = r = 0
        window = defaultdict(int)
        window_sum = res = 0
        while r < len(nums):
            c = nums[r]
            r += 1
            window[c] += 1
            window_sum += c
            while window[c] > 1:
                d = nums[l]
                l += 1
                window[d] -= 1
                window_sum -= d
            res = max(res, window_sum)
        return res
