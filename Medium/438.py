from typing import List
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        cp = Counter(p)
        res = []
        for i in range(len(s) - len(p) + 1):
            sub_s = s[i: i + len(p)]
            if Counter(sub_s) == cp:
                res.append(i)
        return res
