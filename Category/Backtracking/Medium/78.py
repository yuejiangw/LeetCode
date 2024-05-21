from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        
        def backtracking(nums, start_index):
            # 求子集是收集树形结构中树的所有节点的结果，因此
            # 需要提前将 path 加入 res 中
            res.append(path[:])
            if start_index == len(nums):
                return
            for i in range(start_index, len(nums)):
                path.append(nums[i])
                backtracking(nums, i + 1)
                path.pop()

        backtracking(nums, 0)
        return res