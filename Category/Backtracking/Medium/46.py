from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []
        used = [False] * len(nums)
        def backtracking(nums, used):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i in range(len(nums)):
                if used[i] == True: 
                    continue
                used[i] = True
                path.append(nums[i])
                backtracking(nums, used)
                path.pop()
                used[i] = False
        backtracking(nums, used)
        return res