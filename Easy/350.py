from typing import List
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        res = []
        for k, v in c1.items():
            if k in c2:
                res += [k] * min(c1[k], c2[k])
        return res
