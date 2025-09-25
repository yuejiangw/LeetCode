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


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        if not nums:
            return [[lower, upper]]
        # 分组讨论
        res = []
        if nums and nums[0] > lower:
            res.append([lower, nums[0] - 1])

        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] > 1:
                res.append([nums[i - 1] + 1, nums[i] - 1])
        
        if nums and nums[-1] < upper:
            res.append([nums[-1] + 1, upper])
        return res
