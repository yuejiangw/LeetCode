from collections import Counter


class Solution:
    def balancedString(self, s: str) -> int:
        # 第一遍扫描，记录 Q W E R 四个字母中各自超出 n/4 的数量
        cnt = Counter(s)
        n = len(s)

        # 不需要调整任何字符，直接返回 0
        if all(v <= n // 4 for v in cnt.values()):
            return 0

        # 第二遍扫描，滑动窗口判断满足条件的最短子串
        res = float("inf")
        l = 0
        for r, c in enumerate(s):
            cnt[c] -= 1
            while l <= r and all(v <= n // 4 for v in cnt.values()):
                res = min(res, r - l + 1)
                cnt[s[l]] += 1
                l += 1
        return res
