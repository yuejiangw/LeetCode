from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_to_idx = {}
        for idx, n in enumerate(nums):
            if n in num_to_idx:
                if idx - num_to_idx[n] <= k:
                    return True
            num_to_idx[n] = idx
        return False