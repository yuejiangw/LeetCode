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
                # 因为数组已经排好序了，因此如果当前元素加上之前的元素大于 target，那么后面的元素肯定也会大于 target
                # 因此可以直接返回，否则应该用 continue
                if sum(combination) + candidates[i] > target:
                    return
                if i > start_index and candidates[i] == candidates[i - 1]:
                    continue
                combination.append(candidates[i])
                backtracking(candidates, target, i + 1)
                combination.pop()
        backtracking(sorted(candidates), target, 0)
        return res
    
class Solution:
    # 借助 used 数组来去重
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combination = []
        res = []
        used = [False] * len(candidates)

        def backtracking(candidates, sum, start_index, used):
            if sum == target:
                res.append(combination[:])
                return
            for i in range(start_index, len(candidates)):
                # 剪枝
                if sum + candidates[i] > target:
                    return
                # 去重
                # used[i - 1] = False 代表同一树层，
                # used[i - 1] = True 代表同一树枝
                if i > 0 and candidates[i] == candidates[i - 1] and not used[i - 1]:
                    continue
                used[i] = True
                combination.append(candidates[i])
                backtracking(candidates, sum + candidates[i], i + 1, used)
                combination.pop()
                used[i] = False
        
        backtracking(sorted(candidates), 0, 0, used)
        return res