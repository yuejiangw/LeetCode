from typing import List
from collections import Counter

class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s: str):
            return s.count(min(s))
        
        queries_f = [f(query) for query in queries]
        words_f = [f(word) for word in words]
        words_f.sort()
        
        def upper_bound(target, nums):
            l, r = 0, len(nums)
            while l < r:
                m = (l + r) // 2
                if nums[m] <= target:
                    l = m + 1
                else:
                    r = m
            return l
        
        res = []
        for q in queries_f:
            res.append(len(words_f) - upper_bound(q, words_f))
        return res