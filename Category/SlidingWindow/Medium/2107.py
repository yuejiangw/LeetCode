from collections import Counter
from typing import List

class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        '''
        find a fixed-length window, whose candy type is the least
        '''
        candy_type = Counter(candies)
        if k == 0:
            return len(candy_type)
        l = r = 0
        res = 0
        while r < len(candies):
            # expand
            c = candies[r]
            r += 1
            candy_type[c] -= 1
            if candy_type[c] == 0:
                del candy_type[c]
            if r - l < k:
                continue
            # collect
            res = max(res, len(candy_type))
            # shrink
            d = candies[l]
            l += 1
            candy_type[d] += 1
        return res