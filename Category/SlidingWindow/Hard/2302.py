from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        l = r = 0
        res = window = 0
        while r < len(nums):
            c = nums[r]
            r += 1
            window += c
            while l < r and (r - l) * window >= k:
                d = nums[l]
                l += 1
                window -= d
            # 固定右端点 r，那么所有以 r 结尾的子数组 nums[l: r], nums[l+1: r], nums[l+2: r] 都满足条件
            res += r - l
        return res