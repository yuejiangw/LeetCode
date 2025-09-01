from typing import List
from collections import defaultdict

class Solution:
    def longestSubarray(self, nums: List[int], k: int) -> int:
        l = r = 0
        window = defaultdict(int)
        res = 0
        while r < len(nums):
            c = nums[r]
            r += 1
            window[c] += 1
            if window[c] == 2:
                k -= 1
            while l < r and k < 0:
                d = nums[l]
                l += 1
                window[d] -= 1
                if window[d] == 1:
                    k += 1
                if window[d] == 0:
                    del window[d]
            res = max(res, r - l)
        return res