from heapq import *
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        len1 = min(len(nums1), k)
        len2 = min(len(nums2), k)
        for i in range(len1):
            for j in range(len2):
                heappush(heap, [nums1[i], nums2[j]])
        return nsmallest(k, heap, key=sum)
