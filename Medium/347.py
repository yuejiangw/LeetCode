import heapq
from collections import Counter
from typing import List

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
