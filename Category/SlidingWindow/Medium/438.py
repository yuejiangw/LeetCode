from typing import List
from collections import Counter, defaultdict


# 2023-07-10
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # 设 len(s) = m, len(p) = n
        # T: O(n + m * 26)，因为内层循环会遍历 cnt，而 cnt 最多有 26 个元素
        # S: O(26)
        cnt = Counter(p)
        l, r = 0, 0
        res = []
        window = defaultdict(int)
        while r < len(s):
            c = s[r]
            r += 1
            window[c] += 1
            while all(window[k] >= cnt[k] for k in cnt.keys()):
                if window == cnt:
                    res.append(l)
                d = s[l]
                l += 1
                window[d] -= 1
                if window[d] == 0:
                    del window[d]
        return res


# 2021-11-15
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        cp = Counter(p)
        res = []
        for i in range(len(s) - len(p) + 1):
            sub_s = s[i : i + len(p)]
            if Counter(sub_s) == cp:
                res.append(i)
        return res
