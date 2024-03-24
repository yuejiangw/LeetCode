from typing import List


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        i, j = 0, len(nums) - 1
        res = 0
        while i < j:
            while i < j and nums[i] + nums[j] >= target:
                j -= 1
            res += j - i
            i += 1
        return res
