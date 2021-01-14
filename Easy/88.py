class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        n1 = nums1[0:m]
        n2 = nums2[0:n]
        nums1.clear()
        while n1 and n2:
            if n1[0] <= n2[0]:
                nums1.append(n1.pop(0))
            else:
                nums1.append(n2.pop(0))
        if n1:
            nums1 += n1
        if n2:
            nums1 += n2
