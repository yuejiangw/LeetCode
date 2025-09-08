from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 先把 nums2 中的下一个更大元素算出来存在一个表里，再让 nums1 去查表
        def getNextGreaterElement(nums2):
            res = {}
            stack = []
            for i, n in enumerate(nums2):
                while stack and nums2[stack[-1]] < n:
                    idx = stack.pop()
                    res[nums2[idx]] = n
                stack.append(i)
            return res
        
        next_greater_nums2 = getNextGreaterElement(nums2)
        res = []
        for n in nums1:
            if n in next_greater_nums2:
                res.append(next_greater_nums2[n])
            else:
                res.append(-1)
        return res