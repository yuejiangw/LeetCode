class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l = r = 0
        res = 0
        window = {'a': 0, 'b': 0, 'c': 0}
        while r < len(s):
            c = s[r]
            r += 1
            window[c] += 1
            while window['a'] >= 1 and window['b'] >= 1 and window['c'] >= 1:
                d = s[l]
                l += 1
                window[d] -= 1
            # 在退出内层循环之后 s[l-1: r], s[l-2: r], ..., s[0: r] 是合法的
            res += l
        return res