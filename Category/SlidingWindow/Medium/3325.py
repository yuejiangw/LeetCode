from collections import defaultdict

class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        '''
        遇到刚好满足条件的子字符串时, s[l: r], s[l: r+1], ..., s[l: len(s)-1] 都满足条件
        因此在收缩窗口的时候要借助 r 来更新结果
        '''
        l = r = 0
        window = defaultdict(int)
        res = 0
        while r < len(s):
            c = s[r]
            r += 1
            window[c] += 1
            while window[c] == k:
                res += len(s) - r + 1
                d = s[l]
                l += 1
                window[d] -= 1
        return res