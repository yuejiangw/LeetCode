from typing import List

class Solution:
    # 不借助 used 数组来去重
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def backtracking(nums, start):
            res.append(path[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtracking(nums, i + 1)
                path.pop()
        
        # 为了去重，先排序
        backtracking(sorted(nums), 0)
        return res

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
                # 同一树层去重
                if i > 0 and nums[i] == nums[i - 1] and used[i - 1] == False:
                    continue
                path.append(nums[i])
                used[i] = True
                backtracking(i + 1)
                used[i] = False
                path.pop()
        backtracking(0)
        return res
