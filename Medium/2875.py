from typing import List

class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        # 从 target 中减去所有 total 剩下的 remain 才是需要遍历寻找的
        remain = target % total
        l = r = 0
        n = len(nums)
        window = 0
        res = float('inf')
        # 滑动窗口遍历 nums + nums 来避免漏掉循环数组首尾相接时候恰好满足条件的情况
        while r < (2 * n):
            window += nums[r % n]
            r += 1
            while window > remain:
                window -= nums[l % n]
                l += 1
            if window == remain:
                res = min(res, r - l)
        return res + (target // total) * n if res != float('inf') else -1
