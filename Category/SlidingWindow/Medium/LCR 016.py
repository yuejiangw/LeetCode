from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        window = defaultdict(int)
        res = 0
        while r < len(s):
            c = s[r]
            r += 1
            window[c] += 1
            while window[c] > 1:
                d = s[l]
                l += 1
                window[d] -= 1
                if window[d] == 0:
                    del window[d]
            res = max(res, len(window))
        return res