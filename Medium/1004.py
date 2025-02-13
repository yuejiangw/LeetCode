from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # T: O(n), S: O(1)
        res = 0
        i, j = 0, 0
        window = 0
        while j < len(nums):
            c = nums[j]
            j += 1
            if c == 0:
                window += 1
            while window > k:
                d = nums[i]
                i += 1
                if d == 0:
                    window -= 1
            res = max(res, j - i)
        return res
