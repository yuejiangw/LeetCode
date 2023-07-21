from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # 本质上是求不同的正整数数量
        # T: O(n)
        # S: O(n)
        return len(set(nums) - {0})
