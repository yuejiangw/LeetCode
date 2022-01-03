from typing import List


class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def binary_search(nums, target):
            i, j = 0, len(nums)
            while i < j:
                mid = i + (j - i) // 2
                if nums[mid] <= target:
                    i = mid + 1
                else:
                    j = mid
            return 0 if i == len(nums) else i

        nums1.sort()
        res = []
        for num in nums2:
            i = binary_search(nums1, num)
            res.append(nums1.pop(i))
        return res
