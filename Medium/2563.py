from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        '''
        排序后枚举右边的 nums[j]，则 nums[i] 需要满足 lower - nums[j] <= nums[i] <= upper - nums[j]
        可以用 nums[i] <= upper - nums[j] 的数量减去 nums[i] < lower - nums[j] 的数量，利用二分搜索
        T: O(nlogn)
        S: O(1)
        '''
        nums.sort()
        res = 0
        # 注意要在 [0, j-1] 中二分，因为题目要求两个下标 i < j
        for j, num in enumerate(nums):
            # nums[i] > lower - nums[j]
            l = bisect_left(nums, lower - num, 0, j)
            # nums[i] <= upper - nums[j]
            r = bisect_right(nums, upper - num, 0, j)
            res += r - l
        return res
