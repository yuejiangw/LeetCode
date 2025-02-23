from typing import List
from heapq import heappush, heappop
import random

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # T: O(N), S: O(N)

        distances = [(point[0]**2 + point[1]**2, point) for point in points]

        def partition(left, right, pivot_idx):
            pivot_distance = distances[pivot_idx][0]

            # move pivot to the right end
            distances[pivot_idx], distances[right] = distances[right], distances[pivot_idx]

            # move points with less distance to the left
            store_idx = left
            for i in range(left, right):
                if distances[i][0] < pivot_distance:
                    distances[i], distances[store_idx] = distances[store_idx], distances[i]
                    store_idx += 1
            
            distances[store_idx], distances[right] = distances[right], distances[store_idx]
            return store_idx
        
        def quickSelect(left, right, k):
            if left == right:
                return
            
            pivot_idx = random.randint(left, right)
            pivot_idx = partition(left, right, pivot_idx)

            if pivot_idx == k:
                return
            elif k < pivot_idx:
                quickSelect(left, pivot_idx - 1, k)
            else:
                quickSelect(pivot_idx + 1, right, k)
        
        n = len(distances)
        quickSelect(0, n - 1, k)
        return [x[1] for x in distances[:k]]


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