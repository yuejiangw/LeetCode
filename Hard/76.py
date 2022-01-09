from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == t:
            return s
        if len(s) < len(t):
            return ""
        # 记录t中的字符在子序列中出现的次数
        t_char = Counter(t)

        i, j = 0, 0
        res = ''
        min_len = float('inf')

        for j in range(len(s)):
            # 遇到匹配的字符，则t_char中对应字符的计数则-1
            if s[j] in t:
                t_char[s[j]] -= 1

            # t_char中字符数量的最大值小于等于0，代表所有字符都得到了匹配
            while max(t_char.values()) <= 0:
                curr_len = j - i + 1
                if curr_len < min_len:
                    min_len = curr_len
                    res = s[i: j + 1]

                # 滑动窗口的左边界，如果当前字符出现在了t中，则对应的value要+1
                if s[i] in t_char.keys():
                    t_char[s[i]] += 1

                i += 1
        return res


from collections import defaultdict, Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = defaultdict(int)
        need = Counter(t)
        length = float('inf')   # the lenght of the minimum covered substring
        start = 0               # the start index of the minimum covered substring
        valid = 0               # the number of letter that has satisfied the need
        i, j = 0, 0
        while j < len(s):
            # c is going to be added into the window
            c = s[j]
            j += 1
            # update the data inside the window
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            # shrink the left side of the window
            while valid == len(need):
                # update the substring
                if j - i < length:
                    start = i
                    length = j - i
                # d is going to be removed from the window
                d = s[i]
                i += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return '' if length == float('inf') else s[start: start + length]
