from typing import List


class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        maxLen = max([min(rectangle) for rectangle in rectangles])
        res = 0
        for rectangle in rectangles:
            if min(rectangle) >= maxLen:
                res += 1
        return res
