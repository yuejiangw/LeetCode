from typing import List

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        # 贪心 + 前缀和 + 二分
        nums.sort()
        n = len(nums)
        if n > 1:
            for i in range(1, n):
                nums[i] += nums[i - 1]
        
        # 利用二分在前缀和数组上查找 queries[i] + 1 的下界
        def lowerBound(nums, target):
            l, r = 0, len(nums)
            while l < r:
                m = (l + r) // 2
                if nums[m] >= target:
                    r = m
                else:
                    l = m + 1
            return l

        res = []
        for target in queries:
            res.append(lowerBound(nums, target + 1))
        return res
