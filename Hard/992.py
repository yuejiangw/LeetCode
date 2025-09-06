from typing import List
from collections import defaultdict

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        res = r = l1 = l2 = 0
        # different integers >= k 的子数组数量
        window1 = defaultdict(int)
        # different integers > k 的子数组数量
        window2 = defaultdict(int)
        while r < len(nums):
            c = nums[r]
            r += 1
            window1[c] += 1
            window2[c] += 1
            while l1 < r and len(window1) >= k:
                d1 = nums[l1]
                l1 += 1
                window1[d1] -= 1
                if window1[d1] == 0:
                    del window1[d1]
            while l2 < r and len(window2) > k:
                d2 = nums[l2]
                l2 += 1
                window2[d2] -= 1
                if window2[d2] == 0:
                    del window2[d2]
            res += l1 - l2
        return res