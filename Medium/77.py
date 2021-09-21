from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        path = []
        def backtracking(n, k, start_index):
            if len(path) == k:
                result.append(path[:])
                return
            for i in range(start_index, n - (k - len(path)) + 2):
                path.append(i)
                backtracking(n, k, i + 1)
                path.pop()
        backtracking(n, k, 1)
        return result