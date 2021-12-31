from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        arr1 = nums1[: m]
        arr2 = nums2[: n]
        i = 0
        while arr1 and arr2:
            if arr1[0] < arr2[0]:
                nums1[i] = arr1.pop(0)
            else:
                nums1[i] = arr2.pop(0)
            i += 1
        if arr1:
            nums1[i:] = arr1
        if arr2:
            nums1[i:] = arr2


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return

        if m == 0:
            nums1[:] = nums2
            return

        # 逆向双指针
        i, j = m-1, n-1
        tail = len(nums1) - 1
        while j >= 0:
            if i < 0 or nums2[j] >= nums1[i]:
                nums1[tail] = nums2[j]
                j -= 1
            else:
                nums1[tail] = nums1[i]
                i -= 1
            tail -= 1
