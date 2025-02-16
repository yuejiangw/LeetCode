from typing import List


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        res = []
        nums = [lower - 1] + nums + [upper + 1]
        for i in range(len(nums) - 1):
            l, r = nums[i], nums[i + 1]
            if l + 1 <= r - 1:
                res.append([l + 1, r - 1])
        return res
