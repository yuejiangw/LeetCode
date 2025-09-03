class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        res = ''
        window = 0
        l = r = 0
        while r < len(s):
            c = s[r]
            r += 1
            if c == '1':
                window += 1
            while window >= k:
                if window == k:
                    candidate = s[l: r]
                    if not res or len(candidate) < len(res) or (len(candidate) == len(res) and candidate < res):
                        res = candidate
                d = s[l]
                l += 1
                if d == '1':
                    window -= 1

        return res