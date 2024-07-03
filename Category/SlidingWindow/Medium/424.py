class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # 双指针代表窗口的左右边界
        i, j = 0, 0
        window = {}
        max_count = 0   # 存储窗口内个数最多的字符个数
        res = 0
        while j < len(s):
            c = s[j]
            j += 1
            if c not in window:
                window[c] = 0
            window[c] += 1
            max_count = max(max_count, window[c])
            while len(window) >= 2 and j - i - max_count > k:
                d = s[i]
                i += 1
                window[d] -= 1
                if window[d] == 0:
                    del window[d]
            res = max(res, j - i)
        return res