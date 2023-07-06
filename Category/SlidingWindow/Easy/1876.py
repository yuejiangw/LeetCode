from collections import defaultdict


class Solution:
    """
    窗口扩张：窗口内元素计数
    窗口收缩：两种情况，窗口内元素个数大于3或窗口内出现重复元素
    更新结果：窗口内元素数量保证为3的时候计数
    """

    def countGoodSubstrings(self, s: str) -> int:
        i, j = 0, 0
        window = defaultdict(int)
        window_size = 0
        res = 0
        while j < len(s):
            # 窗口扩张
            c = s[j]
            j += 1
            window[c] += 1
            window_size += 1
            # 窗口收缩
            while window_size > 3 or window[c] > 1:
                d = s[i]
                i += 1
                window[d] -= 1
                window_size -= 1
            # 更新结果
            if window_size == 3:
                res += 1
        return res
