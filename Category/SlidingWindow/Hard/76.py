from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnt = Counter(t)
        window = Counter()
        l, r = 0, 0
        res = ""
        res_length = float('inf')
        while r < len(s):
            # 窗口扩张
            right_char = s[r]
            r += 1
            # 把右指针指向的字符放入窗口
            if right_char not in window:
                window[right_char] = 1
            else:
                window[right_char] += 1
            # 窗口收缩
            while window >= cnt:
                # 比较当前 res 长度更新结果
                if res_length > r - l + 1:
                    res = s[l: r]
                    res_length = r - l + 1
                # 窗口左指针指向的字符移出窗口
                left_char = s[l]
                window[left_char] -= 1
                if window[left_char] == 0:
                    del window[left_char]
                l += 1
        return res
