from typing import List
from collections import defaultdict


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        res = 0
        for n in nums:
            if count.get(n + k):
                res += count.get(n + k)
            if count.get(n - k):
                res += count.get(n - k)
            count[n] += 1
        return res
