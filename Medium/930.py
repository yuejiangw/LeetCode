from typing import List

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # l1 用来判断 sum >= goal, l2 用来判断 sum > goal
        l1 = l2 = r = 0
        # res1 用来记录 sum >= goal 的数量, res2 用来记录 sum > goal 的数量, 则 res1 - res2 就是结果
        window1 = window2 = res1 = res2 = 0
        while r < len(nums):
            c = nums[r]
            r += 1
            window1 += c
            window2 += c
            # 判断 sum >= goal
            while l1 < r and window1 >= goal:
                d1 = nums[l1]
                l1 += 1
                window1 -= d1
            while l2 < r and window2 > goal:
                d2 = nums[l2]
                l2 += 1
                window2 -= d2
            res1 += l1
            res2 += l2
        return res1 - res2