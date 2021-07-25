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