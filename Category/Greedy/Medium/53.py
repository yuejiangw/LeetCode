from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Greedy：当连续和为负数的时候立刻放弃，从下一个元素开始重新计算
        res = float('-inf')
        count = 0
        for i in range(len(nums)):
            count += nums[i]
            if count > res:
                res = count
            if count <= 0:
                count = 0
        return res
