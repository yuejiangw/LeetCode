from collections import defaultdict
from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        l = r = 0
        res = 0
        window = defaultdict(int)
        window_sum = 0
        while r < len(nums):
            c = nums[r]
            r += 1
            window[c] += 1
            window_sum += c
            # skip invalid window len
            if r - l < k:
                continue
            # collect
            if len(window) == k:
                res = max(res, window_sum)
            # shrink
            d = nums[l]
            l += 1
            window[d] -= 1
            window_sum -= d
            if window[d] == 0:
                del window[d]
        return res
