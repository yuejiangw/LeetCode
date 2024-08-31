from typing import List
import random

class Solution:
    '''
    w = [1, 3, 5, 1]
    n = 2

    pre_sum = [1, 4, 9, 10]

    w[0] = 1/10
    w[1] = 3/10
    w[2] = 5/10
    w[3] = 1/10
    '''

    def __init__(self, w: List[int]):
        self.pre_sum = []
        self.total_sum = 0

        for weight in w:
            self.total_sum += weight
            self.pre_sum.append(self.total_sum)
        
    def left_bound_search(self, nums, target):
        i, j = 0, len(nums)
        while i < j:
            mid = i + (j - i) // 2
            if nums[mid] >= target:
                j = mid
            elif nums[mid] < target:
                i = mid + 1
        return i

    def pickIndex(self) -> int:
        target = random.randint(1, self.total_sum)
        return self.left_bound_search(self.pre_sum, target)

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()