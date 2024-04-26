import heapq
from collections import Counter
from typing import List

# 2024-04-26
from collections import Counter
from heapq import *

class Solution:
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     # 大顶堆解法, T: O(nlogn), S: O(n)，不是最优
    #     cnt = Counter(nums)
    #     heap = []
    #     res = []
    #     for key, val in cnt.items():
    #         heappush(heap, (-val, key))
        
    #     for _ in range(k):
    #         res.append(heappop(heap)[1])
    #     return res

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 小顶堆解法，T: O(nlogk), S: O(n)
        cnt = Counter(nums)
        heap = []
        for key, val in cnt.items():
            heappush(heap, (val, key))
            if len(heap) > k:
                heappop(heap)
        # 最后堆中剩下的就是前 k 个大的数
        return [item[1] for item in heap]

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        for n in nums:
            if n not in hash_map.keys():
                hash_map[n] = 1
            else:
                hash_map[n] += 1
        # 关键：将字典按照值的大小关系降序排序
        buckets = sorted(hash_map.items(), key=lambda x: x[1], reverse=True)
        results = []
        for i in range(k):
            results.append(buckets[i][0])
        return results


class Solution:
    """利用heapq构造小顶堆"""
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        pri_queue = []
        for key, count in counter.items():
            heapq.heappush(pri_queue, (count, key))
            if len(pri_queue) > k:
                heapq.heappop(pri_queue)

        res = [0] * k
        for i in range(k - 1, -1, -1):
            res[i] = heapq.heappop(pri_queue)[1]
        return res


from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # top k: use min heap. Every time we want to push a element into the heap,
        # First we should compare it with the top of the heap. If the element is
        # smaller than the heap top, then discard it. Otherwise, replace the heap
        # top to the element.
        freq = Counter(nums)
        heap = []
        for key, val in freq.items():
            heapq.heappush(heap, (val, key))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res