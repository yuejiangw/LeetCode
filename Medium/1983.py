from typing import List


class Solution:
    def widestPairOfIndices(self, nums1: List[int], nums2: List[int]) -> int:
        # nums1[i] + nums1[i+1] + ... + nums1[j] == nums2[i] + nums2[i+1] + ... + nums2[j]
        # can be rewritten in:
        # (nums1[i]-nums2[i]) + (nums1[i+1]-nums2[i+1]) + ... + (nums1[j]-nums2[j]) == 0
        # compute the difference of prefix sum of the two arrays, and record the index of   
        # the difference first appears using a hash map. If the same value appears again, then
        # the value of current index - pre index + 1 is a potential result. Collect all the
        # potential results and return the max one.
        prefix_map = {0: 0}
        prefix_sum = 0
        length = len(nums1)
        res = 0
        for i in range(length):
            prefix_sum += (nums1[i] - nums2[i])
            if prefix_sum in prefix_map:
                res = max(res, i - prefix_map[prefix_sum] + 1)
            else:
                prefix_map[prefix_sum] = i + 1
        return res