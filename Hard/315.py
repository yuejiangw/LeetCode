from typing import List
from sortedcontainers import SortedList
from bisect import bisect_left

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # T: O(n * sigma(log^2(k))), k = 1, 2, ..., n
        # S: O(n)
        l = SortedList()
        res = []
        for num in nums[::-1]:
            loc = bisect_left(l, num)
            l.add(num)
            res.append(loc)
        return res[::-1]