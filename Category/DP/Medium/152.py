from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # DP, T = O(n), S = O(1)
        # 需要同时维护当前最小值和当前最大值，遇到负数的时候把二者交换
        res = nums[0]
        max_num = nums[0]
        min_num = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                max_num, min_num = min_num, max_num
            max_num = max(max_num * nums[i], nums[i])
            min_num = min(min_num * nums[i], nums[i])
            res = max(res, max_num)
        return res
        