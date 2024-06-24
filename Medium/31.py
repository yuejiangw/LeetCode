from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 贪心的思想，借助双指针实现
        # 本质上是找到左边的一个较小数和右边的一个较大数并交换，同时要求左边较小数要尽可能靠右，右边较大数要尽可能小
        i = len(nums) - 2
        # 找左边一个较小数
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            # 找右边一个较大数
            j = len(nums) - 1
            while j > i and nums[i] >= nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
