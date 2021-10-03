from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        used = [False] * len(nums)
        def backtracking(nums, used):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1] and used[i - 1] == False:
                    continue
                if used[i] == False:
                    used[i] = True
                    path.append(nums[i])
                    backtracking(nums, used)
                    path.pop()
                    used[i] = False
        backtracking(sorted(nums), used)
        return res