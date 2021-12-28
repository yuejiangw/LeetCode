from typing import List
from collections import deque


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        length = len(heights)
        res = deque([length - 1])
        min_height = heights[length - 1]
        for i in range(length - 2, -1, -1):
            if heights[i] > min_height:
                res.appendleft(i)
                min_height = heights[i]
        return list(res)
