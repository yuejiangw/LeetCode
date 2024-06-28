from typing import List

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        i, j = 0, 0
        res = 0
        window = {}
        
        while j < len(nums):
            # 窗口右移
            c = nums[j]
            j += 1
            # 更新窗口计数
            if c not in window:
                window[c] = 0
            window[c] += 1
            # 重复元素次数 > k，窗口收缩
            while window[c] > k:
                d = nums[i]
                i += 1
                window[d] -= 1
            res = max(res, j - i)
        return res