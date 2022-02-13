from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """ 单调栈 + 哈希表, 时间复杂度 O(len(nums1) + len(nums2)) """
        idx_map = {}
        stack = []
        for n in nums2:
            while stack and n > stack[-1]:
                idx_map[stack.pop()] = n
            stack.append(n)
        while stack:
            idx_map[stack.pop()] = -1
        return [idx_map[x] for x in nums1]
