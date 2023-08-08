from itertools import accumulate
from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        """
        子数组的和等于两个前缀和的差，取前缀和中的最大值和最小值作差就是答案
        """
        s = list(accumulate(nums, initial=0))  # nums 的前缀和
        return max(s) - min(s)
