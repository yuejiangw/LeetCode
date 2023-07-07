class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num = str(num)
        l, r = 0, 0
        window = ""
        res = 0
        # 窗口扩张
        while r < len(num):
            c = num[r]
            r += 1
            window += c
            # 窗口收缩
            if len(window) > k:
                d = num[l]
                l += 1
                window = window[1:]
            # 更新结果
            if len(window) == k and int(window) != 0 and int(num) % int(window) == 0:
                res += 1
        return res
