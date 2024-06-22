from typing import List
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        有个坑: 在遍历 cnt 的时候不能用 k 作为 key 的遍历值，会覆盖参数中的 k
        """
        cnt = Counter(nums)
        heap = []
        for key, val in cnt.items():
            heapq.heappush(heap, (val, key))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res