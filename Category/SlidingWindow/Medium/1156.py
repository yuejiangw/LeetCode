from collections import Counter


class Solution:
    def maxRepOpt1(self, text: str) -> int:
        cnt = Counter(text)
        n = len(text)
        res = 0
        i = 0
        while i < n:
            # 从 i 开始扫描所有与 text[i] 相同的字符
            j = i
            while j < n and text[j] == text[i]:
                j += 1
            # 该子串的范围是 text[i...j - 1]
            l = j - i
            # 接下来我们跳过 j 指向的字符，用 k 继续向右移动
            # 直到 k 指向的字符与 i 指向的字符不同
            k = j + 1
            while k < n and text[k] == text[i]:
                k += 1
            # 这个子串的长度为 k - j - 1
            r = k - j - 1
            # 更新结果
            # min(l + r + 1, cnt[text[i]]) 是为了防止出现 aaabaaa 的情况
            res = max(res, min(l + r + 1, cnt[text[i]]))
            i = j
        return res
