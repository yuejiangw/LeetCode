from typing import List
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = sorted(points, key=lambda x: pow(x[0], 2) + pow(x[1], 2))
        return points[:k]
