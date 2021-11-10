from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """暴力，时间复杂度O(nlogn)"""
        newNums = [abs(num) for num in nums]
        newNums.sort()
        return [n ** 2 for n in newNums]


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """双指针，时间复杂度O(n)"""
        res = [0] * len(nums)
        i, j = 0, len(nums) - 1
        idx = len(nums) - 1
        while i <= j:
            pi = nums[i] * nums[i]
            pj = nums[j] * nums[j]
            if pi < pj:
                res[idx] = pj
                j -= 1
            else:
                res[idx] = pi
                i += 1
            idx -= 1
        return res
