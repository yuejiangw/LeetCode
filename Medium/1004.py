from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # Sliding Window, 找出一个最长的子数组, 该子数组内最多允许有 k 个0
        # T: O(N)
        # S: O(1)
        res = 0
        window = 0
        i, j = 0, 0
        while j < len(nums):
            c = nums[j]
            j += 1
            if c == 0:
                window += 1
            if window <= k:
                res = max(res, j - i)
            while i < j and window > k:
                d = nums[i]
                i += 1
                if d == 0:
                    window -= 1
        return res
