from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # T: O(N^2)
        # S: O(logN)
        
        if len(nums) < 3:
            return 0
        nums.sort()

        def two_sum_closest(nums, start, target):
            i, j = start, len(nums) - 1
            delta = float('inf')
            while i < j:
                sum = nums[i] + nums[j]
                if abs(delta) > abs(target - sum):
                    delta = target - sum
                if sum < target:
                    i += 1
                else:
                    j -= 1
            return target - delta

        delta = float('inf')
        for i in range(len(nums) - 2):
            sum = nums[i] + two_sum_closest(nums, i + 1, target - nums[i])
            if abs(delta) > abs(target - sum):
                delta = target - sum
        return target - delta
