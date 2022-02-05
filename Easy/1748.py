from typing import List
from collections import Counter


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        count = Counter(nums)
        return sum([num for num in nums if count[num] == 1])
