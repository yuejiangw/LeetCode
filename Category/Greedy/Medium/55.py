from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Greedy，假设我们在位置 i 起跳，可以选择的步长是 nums[i]
        # 跳跃的终点要选择 nums[i + 1: i + nums[i] + 1] 中最大的那个数
        # 本质上是判断跳跃覆盖范围是否可以到终点
        if len(nums) <= 1:
            return True
        i = 0
        cover = 0
        while i <= cover:
            cover = max(cover, i + nums[i])
            if cover >= len(nums) - 1:
                return True
            i += 1
        return False
