from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # T: O(n), S: O(1)
        if len(nums) == 1:
            return 1
        store_idx, i = 1, 1
        while i < len(nums):
            if nums[i] != nums[i - 1]:
                nums[store_idx] = nums[i]
                store_idx += 1
            i += 1
        return store_idx