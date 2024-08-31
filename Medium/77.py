from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []

        def backtracking(start):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(start, n + 1):
                path.append(i)
                backtracking(i + 1)
                path.pop()
        
        backtracking(1)
        return res