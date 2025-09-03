from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnt = Counter(t)
        uncover = len(cnt)
        window = defaultdict(int)
        l = r = 0
        res = ''
        while r < len(s):
            c = s[r]
            r += 1
            window[c] += 1
            if c in cnt:
                cnt[c] -= 1
                if cnt[c] == 0:
                    # cnt[c] == 0 代表一个新的字符被完全 cover
                    uncover -= 1
            while uncover <= 0:
                if uncover == 0:
                    res = min(res, s[l: r], key=len) if res != '' else s[l: r]
                d = s[l]
                l += 1
                if d in cnt:
                    cnt[d] += 1
                    if cnt[d] == 1:
                        # cnt[d] == 1 代表一个新字符被 uncover 了
                        uncover += 1
        return res