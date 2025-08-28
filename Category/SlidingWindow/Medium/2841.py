from collections import defaultdict
from typing import List

class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        l = r = 0
        res = 0
        window = defaultdict(int)
        window_sum = 0
        while r < len(nums):
            # expand
            c = nums[r]
            r += 1
            window[c] += 1
            window_sum += c
            if r - l < k:
                continue
            # collect
            if len(window) >= m:
                res = max(res, window_sum)
            # shrink
            d = nums[l]
            l += 1
            window[d] -= 1
            if window[d] == 0:
                del window[d]
            window_sum -= d
        return res
