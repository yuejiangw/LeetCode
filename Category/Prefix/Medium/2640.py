from typing import List

class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        
        # init
        curr_max = nums[0]
        curr_conver = nums[0] + curr_max
        res[0] = curr_conver

        for i in range(1, len(nums)):
            curr_max = max(curr_max, nums[i])
            curr_conver = nums[i] + curr_max
            res[i] = res[i - 1] + curr_conver

        return res