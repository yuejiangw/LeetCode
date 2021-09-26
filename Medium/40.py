from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combination = []
        res = []
        def backtracking(candidates, target, start_index):
            if sum(combination) == target:
                res.append(combination[:])
                return
            for i in range(start_index, len(candidates)):
                if sum(combination) + candidates[i] > target:
                    return
                if i > start_index and candidates[i] == candidates[i - 1]:
                    continue
                combination.append(candidates[i])
                backtracking(candidates, target, i + 1)
                combination.pop()
        backtracking(sorted(candidates), target, 0)
        return res