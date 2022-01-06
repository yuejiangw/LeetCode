from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        path = []
        used = [False] * len(nums)

        def backtracking(start):
            res.append(path[:])
            if start == len(nums):
                return
            for i in range(start, len(nums)):
                if i > 0 and nums[i] == nums[i - 1] and used[i - 1] == False:
                    continue
                path.append(nums[i])
                used[i] = True
                backtracking(i + 1)
                used[i] = False
                path.pop()
        backtracking(0)
        return res
