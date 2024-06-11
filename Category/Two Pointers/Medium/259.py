from typing import List


class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        def twoSumSmaller(nums, target, start):
            i, j = start, len(nums) - 1
            count = 0
            while i < j:
                if nums[i] + nums[j] < target:
                    # nums[i] 和 nums[i+1:j+1] 中的任何一个元素之和都小于 target
                    count += j - i
                    i += 1
                else:
                    j -= 1
            return count
        
        nums.sort()
        res = 0
        for i in range(len(nums) - 2):
            res += twoSumSmaller(nums, target - nums[i], i + 1)
        return res