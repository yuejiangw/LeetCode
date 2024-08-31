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

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''贪心思路
        尽可能到达最远位置
        如果一个位置可达，则它之前的所有位置都可达
        '''
        max_cover = 0
        for i, num in enumerate(nums):
            # 如果当前位置可达并且当前位置 + 跳数 > 最远位置，则更新最远位置
            if max_cover >= i and i + num > max_cover:
                max_cover = i + num
        return max_cover >= len(nums) - 1