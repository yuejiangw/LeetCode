from typing import List
import random


class Solution:

    def __init__(self, w: List[int]):
        n = len(w)
        self.pre_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            self.pre_sum[i] = self.pre_sum[i - 1] + w[i - 1]

    def left_bound_search(self, nums, target):
        if len(nums) == 0:
            return -1
        i, j = 0, len(nums)
        while i < j:
            mid = i + (j - i) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                j = mid
            elif nums[mid] < target:
                i = mid + 1
        return i
    
    def pickIndex(self) -> int:
        target = random.randint(1, self.pre_sum[-1])
        return self.left_bound_search(self.pre_sum, target) - 1


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()