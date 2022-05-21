from typing import List


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        s = set()
        res = 0
        for n in nums:
            if n not in s:
                s.add(n)
            else:
                res = n
                break
        return res