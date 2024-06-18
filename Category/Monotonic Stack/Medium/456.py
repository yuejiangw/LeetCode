from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        min_val = float('-inf')
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < min_val:
                return True
            while stack and stack[-1] < nums[i]:
                min_val = stack.pop()
            stack.append(nums[i])
        return False
