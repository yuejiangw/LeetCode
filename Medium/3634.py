from typing import List

class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        '''
        找到一个 subarray，使该子数组是平衡的而且该 subarray 最长
        则 len(nums) - len(subarray) 就是我们想要移除的最小元素数量
        '''
        if len(nums) == 1:
            return 0
        l = r = 0
        res = 0
        nums.sort()
        while r < len(nums):
            c = nums[r]
            r += 1
            # shrink window
            while l < r and nums[l] * k < c:
                l += 1
            # collect
            res = max(res, r - l)
        return len(nums) - res