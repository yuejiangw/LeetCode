from math import *
from typing import List


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for _ in range(k):
            target = max(gifts)
            idx = gifts.index(target)
            if target <= 1:
                break
            gifts[idx] = floor(sqrt(target))
        return sum(gifts)
