from typing import List
from heapq import heappush, heappop

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # T: O(Nlogk), S:O(k)
        def get_distance(point: List[int]):
            x, y = point
            return x * x + y * y
        
        heap = [] # max heap
        for point in points:
            distance = get_distance(point)
            heappush(heap, [-distance, point])
            if len(heap) > k:
                heappop(heap)
        
        return [x[1] for x in heap]