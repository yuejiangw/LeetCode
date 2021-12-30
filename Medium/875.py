import math
from typing import List


class Solution:
    def finish_time(self, k, piles):
        time = 0
        for pile in piles:
            if pile < k:
                time += 1
            else:
                time += math.ceil(pile / k)
        return time

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        i, j = 1, max(piles) + 1
        while i < j:
            mid = i + (j - i) // 2
            if self.finish_time(mid, piles) <= h:
                j = mid
            elif self.finish_time(mid, piles) > h:
                i = mid + 1
        return i
