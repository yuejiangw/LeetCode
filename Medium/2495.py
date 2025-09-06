from typing import List

class Solution:
    def evenProduct(self, nums: List[int]) -> int:
        # 使用滑动窗口找到恰好乘积不为偶数的左端点
        l = r = 0
        window = 1
        res = 0
        while r < len(nums):
            c = nums[r]
            r += 1
            window *= c
            while window % 2 == 0:
                d = nums[l]
                l += 1
                window //= d
            res += l
        return res