class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        l = r = 0
        window = [0, 0] # [count 0, count 1]
        res = 0
        while r < len(s):
            c = s[r]
            r += 1
            window[int(c)] += 1
            while window[0] > k and window[1] > k:
                d = s[l]
                l += 1
                window[int(d)] -= 1
            res += r - l
        return res