from collections import defaultdict
from typing import List

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # 两两一组，首先遍历 nums1 和 nums2 来记录元素和，之后遍历 nums3 和 nums4 来判断哈希表中是否有和为 0 的元素对
        # 分治思想，T: O(N^2)
        cache = defaultdict(int)
        res = 0
        for m in nums1:
            for n in nums2:
                cache[m + n] += 1
        for m in nums3:
            for n in nums4:
                if -(m + n) in cache:
                    res += cache[-(m + n)]
        return res