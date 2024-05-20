from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        res = []

        # 通过 start index 来控制不收集重复的结果
        def backtracking(start, sum):
            # 收集结果
            if sum == target:
                res.append(path[:])
                return
            for i in range(start, len(candidates)):
                # 剪枝
                if sum + candidates[i] > target:
                    continue
                path.append(candidates[i])
                backtracking(i, sum + candidates[i])
                path.pop()
        
        backtracking(0, 0)
        return res