from typing import List


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        # Brute Force
        # T: O(N^2)
        # S: O(N)
        res = float('inf')
        memo = set()
        for x1, y1 in points:
            for x2, y2 in memo:
                if (x2, y1) in memo and (x1, y2) in memo:
                    res = min(res, abs(x2 - x1) * abs(y2 - y1))
            memo.add((x1, y1))
        return res if res != float('inf') else 0