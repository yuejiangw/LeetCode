from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # l1, window1 容纳奇数数字 >= k 的子数组数目
        # l2, window2 容纳奇数数字 > k 的子数组数目
        l1 = l2 = r = 0
        window1 = window2 = res = 0
        while r < len(nums):
            c = nums[r]
            r += 1
            if c % 2 == 1:
                window1 += 1
                window2 += 1
            while window1 >= k:
                d1 = nums[l1]
                l1 += 1
                if d1 % 2 == 1:
                    window1 -= 1
            while window2 > k:
                d2 = nums[l2]
                l2 += 1
                if d2 % 2 == 1:
                    window2 -= 1
            res += l1 - l2
        return res