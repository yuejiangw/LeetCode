from typing import List

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        '''
        find the lower bounds of 0 and 1
        '''
        def lowerBound(nums, target):
            l, r = 0, len(nums)
            while l < r:
                mid = (l + r) // 2
                if nums[mid] >= target:
                    r = mid
                else:
                    l = mid + 1
            return l
        
        lower_0 = lowerBound(nums, 0)
        lower_1 = lowerBound(nums, 1)
        return max(lower_0, len(nums) - lower_1)
        