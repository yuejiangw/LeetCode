from typing import List
from collections import defaultdict
import bisect

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        num_to_idx = defaultdict(list)
        for i, num in enumerate(nums):
            num_to_idx[num].append(i)
        n = len(nums)
        res = []
        
        for q in queries:
            ans = 0
            num = nums[q]
            indices = num_to_idx[num]
            l = len(indices)
            if l == 1:
                ans = -1
            else:
                i = bisect.bisect_left(indices, q)
                if i == 0:
                    ans = min(indices[i + 1] - indices[i], n - indices[-1] + indices[i])
                elif i == l - 1:
                    ans = min(indices[i] - indices[i - 1], n - indices[i] + indices[0])
                else:
                    ans = min(indices[i] - indices[i - 1], indices[i + 1] - indices[i])
            res.append(ans)
        return res