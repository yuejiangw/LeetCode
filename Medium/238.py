from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left = [0] * length
        right = [0] * length

        left[0] = nums[0]
        for i in range(1, length):
            left[i] = left[i-1] * nums[i]

        right[-1] = nums[-1]
        for i in range(length-2, -1, -1):
            right[i] = right[i+1] * nums[i]

        res = [0] * length
        res[0] = right[1]
        res[-1] = left[-2]
        for i in range(1, length-1):
            res[i] = left[i-1] * right[i+1]

        return res
