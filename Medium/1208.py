class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        l = r = 0
        res = 0 
        while r < len(s):
            c1, c2 = s[r], t[r]
            r += 1
            maxCost -= abs(ord(c1) - ord(c2))
            while l < r and maxCost < 0:
                d1, d2 = s[l], t[l]
                l += 1
                maxCost += abs(ord(d1) - ord(d2))
            res = max(res, r - l)
        return res