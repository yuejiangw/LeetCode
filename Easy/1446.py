class Solution:
    def maxPower(self, s: str) -> int:
        res = 1
        i = 0
        while i < len(s) - 1:
            j = i + 1
            while j < len(s) and s[j] == s[i]:
                j += 1
            res = max(res, j - i)
            i = j
        return res
