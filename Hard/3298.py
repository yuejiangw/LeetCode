from collections import defaultdict, Counter

class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        l = r = 0
        window = defaultdict(int)
        cnt = Counter(word2)
        cover = 0
        res = 0
        while r < len(word1):
            c = word1[r]
            r += 1
            window[c] += 1
            if c in cnt and window[c] == cnt[c]:
                cover += 1
            while cover == len(cnt):
                d = word1[l]
                l += 1
                window[d] -= 1
                if d in cnt and window[d] == cnt[d] - 1:
                    cover -= 1
            res += l
        return res
