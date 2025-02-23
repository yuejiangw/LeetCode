from typing import List
from collections import Counter
import heapq
import random

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 快速选择，时间复杂度 O(n)，空间复杂度 O(n)
        freq = list(Counter(nums).items())

        def partition(left, right, pivot_idx):
            pivot_freq = freq[pivot_idx][1]
            # move the pivot to the end
            freq[pivot_idx], freq[right] = freq[right], freq[pivot_idx]
            # move all less frequent elements to the left
            store_idx = left
            for i in range(left, right):
                if freq[i][1] < pivot_freq:
                    freq[store_idx], freq[i] = freq[i], freq[store_idx]
                    store_idx += 1
            # move the pivot back to its final place
            freq[store_idx], freq[right] = freq[right], freq[store_idx]
            return store_idx

        def quickSelect(left, right, k):
            # base case: list contains only 1 element
            if left == right:
                return
            
            # select a random pivot index
            pivot_idx = random.randint(left, right)

            # find the pivot position in a sorted list
            pivot_idx = partition(left, right, pivot_idx)

            if k == pivot_idx:
                return
            elif k < pivot_idx:
                quickSelect(left, pivot_idx - 1, k)
            else:
                quickSelect(pivot_idx + 1, right, k)

        n = len(freq)
        # kth top freq element is (n-k)th less freq
        quickSelect(0, n - 1, n - k)
        return [x[0] for x in freq[n - k:]]


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