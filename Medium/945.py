from typing import List


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        # T: O(N)
        # S: O(N)
        n = len(nums)
        frequency = [0] * (n + max(nums) + 1)
        res = 0

        for num in nums:
            frequency[num] += 1
        
        for i in range(len(frequency)):
            if frequency[i] <= 1:
                continue
            
            duplicates = frequency[i] - 1
            frequency[i + 1] += duplicates
            frequency[i] = 1
            res += duplicates
        return res