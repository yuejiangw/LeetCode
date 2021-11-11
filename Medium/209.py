from typing import List

class Solution:
    """暴力，时间复杂度O(n^2)，超时"""
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        for i in range(len(nums)):
            j = i + 1
            while j <= len(nums):
                sub_array = nums[i: j]
                sum_sub = sum(sub_array)
                if sum_sub < target:
                    j += 1
                else:
                    res = min(res, j - i)
                    break
        return res if res != float('inf') else 0


class Solution:
    """滑动窗口，时间复杂度O(n)"""
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        sum_array = 0
        idx = 0
        for i in range(len(nums)):
            sum_array += nums[i]
            while sum_array >= target:
                res = min(res, i - idx + 1)
                sum_array -= nums[idx]
                idx += 1
        return res if res != float('inf') else 0
