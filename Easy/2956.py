from typing import List

class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # T: O(M + N), S: O(M + N)
        # 如果用暴力，则 T 是 O(M * N)，S 是 O(1)
        def common_element_num(nums, nums_set) -> int:
            res = 0
            for num in nums:
                if num in nums_set:
                    res += 1
            return res

        set_1, set_2 = set(nums1), set(nums2)
        res1, res2 = common_element_num(nums1, set_2), common_element_num(nums2, set_1)
        return [res1, res2]