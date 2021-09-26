from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        nums = []
        def backtracking(candidates, target, start_index):
            if sum(nums) > target:
                return
            if sum(nums) == target:
                res.append(list(nums)[:])
                return

            i = start_index
            while i < len(candidates) and sum(nums) + candidates[i] <= target:
                nums.append(candidates[i])
                backtracking(candidates, target, i)
                nums.pop()
                i += 1
        backtracking(sorted(candidates), target, 0)
        return res