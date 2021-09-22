from typing import List
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        path = []
        result = []
        def backtracking(k, n, start_index):
            # 剪枝
            if sum(path) > n:
                return
            # 回溯终止条件
            if len(path) == k:
                if sum(path) == n:
                    result.append(path[:])
                return
            for i in range(start_index, 10):
                path.append(i)
                backtracking(k, n, i + 1)
                path.pop()
            return result
        backtracking(k, n, 1)
        return result