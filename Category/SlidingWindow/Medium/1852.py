from typing import List
from collections import defaultdict

class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        l = r = 0
        window = defaultdict(int)
        res = []
        while r < len(nums):
            c = nums[r]
            r += 1
            window[c] += 1
            if r - l < k:
                continue
            res.append(len(window))
            d = nums[l]
            l += 1
            window[d] -= 1
            if window[d] == 0:
                del window[d]
        return res
