class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        if set(s) == set(t):
            for c in set(s):
                if s.count(c) != t.count(c):
                    return False
            return True
        else:
            return False
        
# 2024.04.12
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)