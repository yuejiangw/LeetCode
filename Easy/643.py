from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # T: O(N), S: O(1)
        i, j = 0, 0
        res = float('-inf')
        window = 0
        while j < len(nums):
            c = nums[j]
            j += 1
            window += c
            if j - i == k:
                res = max(res, window / k)
            while j - i >= k:
                d = nums[i]
                i += 1
                window -= d
        return res