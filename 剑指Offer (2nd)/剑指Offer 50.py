class Solution:
    def firstUniqChar(self, s: str) -> str:
        for c in list(s):
            if s.count(c) == 1:
                return c
        return ' '