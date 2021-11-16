from typing import List
from collections import defaultdict

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter2 = defaultdict(str)
        for num in nums2:
            if num not in counter2:
                counter2[num] = 1
            else:
                counter2[num] += 1
        res = []
        for n in set(nums1):
            if counter2[n] != '':
                res.append(n)
        return res
