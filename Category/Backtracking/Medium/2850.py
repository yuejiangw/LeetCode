from typing import List

class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        def permutations(nums):
            res = []
            path = []
            used = [False] * len(nums)

            def backtracking(nums):
                if len(path) == len(nums):
                    res.append(path[:])
                    return
                for i in range(len(nums)):
                    if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                        continue
                    if not used[i]:
                        used[i] = True
                        path.append(nums[i])
                        backtracking(nums) 
                        used[i] = False
                        path.pop()
            
            backtracking(sorted(nums))
            return res

        more = []
        less = []
        for i in range(3):
            for j in range(3):
                if grid[i][j] > 1:
                    more.extend([(i, j)] * (grid[i][j] - 1))
                elif grid[i][j] == 0:
                    less.append((i, j))
        
        res = float('inf')
        for perms in permutations(more):
            steps = 0
            for (px, py), (lx, ly) in zip(perms, less):
                steps += abs(px - lx) + abs(py - ly)
            res = min(res, steps)
        return res