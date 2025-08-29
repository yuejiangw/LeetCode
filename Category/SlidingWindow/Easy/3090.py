from collections import defaultdict

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        l = r = 0
        res = 0
        window = defaultdict(int)
        while r < len(s):
            c = s[r]
            r += 1
            window[c] += 1
            while window[c] > 2:
                d = s[l]
                l += 1
                window[d] -= 1
                if window[d] == 0:
                    del window[d]
            res = max(res, r - l)
        return res