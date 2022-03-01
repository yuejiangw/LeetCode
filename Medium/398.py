from typing import List
import random


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        count = 0
        res = -1
        for i in range(len(self.nums)):
            if self.nums[i] == target:
                if random.randint(0, count) == 0:
                    res = i
                count += 1
        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)