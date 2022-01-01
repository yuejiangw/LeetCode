from typing import List


class Solution:
    def get_max(self, nums, i):
        """ Get the first ith maximum numbers from nums List. """
        if i == 0:
            return []

        stack = []
        abort_num = len(nums) - i
        for n in nums:
            while stack and abort_num and stack[-1] < n:
                stack.pop()
                abort_num -= 1
            stack.append(n)
        return stack[:i]

    def merge(self, nums1, nums2, k):
        """ merge two lists into the largest list """
        if not nums1:
            return nums2
        if not nums2:
            return nums1
        return [max(nums1, nums2).pop(0) for _ in range(k)]

    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        """
        1. for loop
        2. num1 -> get max i numbers, num2 -> get max (k - i) nums
        3. merge the elected numbers into a temporary result
        4. get the final result from all the temporary results
        """
        res = [0] * k
        for i in range(k + 1):
            if i <= len(nums1) and (k - i) <= len(nums2):
                candidate_1 = self.get_max(nums1, i)
                candidate_2 = self.get_max(nums2, k - i)
                candidate = self.merge(candidate_1, candidate_2, k)
                if res < candidate:
                    res = candidate
        return res
