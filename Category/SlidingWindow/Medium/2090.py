from typing import List

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        # window size = 2k + 1
        l = r = 0
        window = 0
        res = [-1] * len(nums)
        radius = 2 * k + 1
        while r < len(nums):
            # expand
            c = nums[r]
            r += 1
            window += c
            # skip invalid size
            if r - l < radius:
                continue
            # collect
            idx = l + k
            res[idx] = window // radius
            # shrink
            d = nums[l]
            l += 1
            window -= d
        return res