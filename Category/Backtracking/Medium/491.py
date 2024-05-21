from typing import List

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []
        def backtracking(nums, start_index):
            if len(path) > 1:
                res.append(path[:])
            # 去重条件：同一父节点下同层上使用过的元素就不能再使用了
            used = set()
            for i in range(start_index, len(nums)):
                if (len(path) > 0 and nums[i] < path[-1]) or nums[i] in used:
                    continue
                used.add(nums[i])
                path.append(nums[i])
                backtracking(nums, i + 1)
                path.pop()
        
        backtracking(nums, 0)
        return res