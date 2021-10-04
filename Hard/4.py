from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sortedArray = []
        while nums1 and nums2:
            if nums1[0] <= nums2[0]:
                sortedArray.append(nums1.pop(0))
            else:
                sortedArray.append(nums2.pop(0))
        if nums1:
            sortedArray += nums1
        if nums2:
            sortedArray += nums2
        length = len(sortedArray)
        return sortedArray[length // 2] if length % 2 == 1 else \
            0.5 * (sortedArray[length // 2 - 1] + sortedArray[length // 2])