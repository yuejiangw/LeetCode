from typing import List
from collections import defaultdict

class Solution:
    def beautifulBouquet(self, flowers: List[int], cnt: int) -> int:
        l = r = 0
        window = defaultdict(int)
        res = 0
        while r < len(flowers):
            c = flowers[r]
            r += 1
            window[c] += 1
            while window[c] > cnt:
                d = flowers[l]
                l += 1
                window[d] -= 1
            res += r - l
        return res