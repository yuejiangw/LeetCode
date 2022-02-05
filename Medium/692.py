import heapq
from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = Counter(words)
        heap = []
        # heappush 可以接受一个 tuple 或 list, tuple 或 list的第一个元素视为 priority key.
        # 由于heapq默认是小顶堆, 因此以 -val 作为 priority key, 则可以将其转换为大顶堆
        for key, val in counts.items():
            heapq.heappush(heap, (-val, key))
        return [heapq.heappop(heap)[1] for _ in range(k)]
