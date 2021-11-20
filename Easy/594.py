from typing import List
from collections import Counter

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counts = {}
        # 对nums中的每个数字进行计数
        for n in nums:
            if n not in counts.keys():
                counts[n] = 1
            else:
                counts[n] += 1
        results = []
        res = 0
        # 对于当前数字k，如果k+1也在哈希表中，则以k开头的和谐数组的长度为k的数量+(k+1)的数量
        # 如果k+1不在哈希表中，则以k开头的和谐数组的长度为0
        for k, v in counts.items():
            res = 0 if k+1 not in counts.keys() else v+counts[k+1]
            results.append(res)
        return max(results)


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        res = 0
        nums = Counter(nums)
        for k, v in nums.items():
            if k + 1 in nums:
                res = max(res, v + nums[k + 1])
        return res
