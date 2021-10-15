from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) == 2:
            return min(height)
        i = 0 
        j = len(height) - 1
        res = 0
        while i < j:
            h = min(height[i], height[j])
            res = max(res, h * (j - i))
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return res