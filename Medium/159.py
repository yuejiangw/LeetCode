class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        # sliding window
        i, j = 0, 0
        window = {}
        res = 0
        curr_max = 0
        while j < len(s):
            # 窗口右移
            c = s[j]
            j += 1
            # 更新窗口内元素计数器
            if c not in window:
                window[c] = 0
            window[c] += 1
            curr_max += 1
            # 窗口收缩
            while len(window) > 2:
                d = s[i]
                i += 1
                window[d] -= 1
                curr_max -= 1
                if window[d] == 0:
                    del window[d]
            # 收集结果
            res = max(res, curr_max)
        return res