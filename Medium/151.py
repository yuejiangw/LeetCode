class Solution:
    def reverseWords(self, s: str) -> str:
        """正常做法，不调用任何api"""
        # 去掉首尾空格
        i, j = 0, len(s) - 1
        while i < j and s[i] == ' ':
            i += 1
        while i < j and s[j] == ' ':
            j -= 1
        s = s[i: j + 1]
        # 去掉单词中间多余空格
        tmp = []
        m, n = 0, 0
        while n < len(s):
            if s[n] != ' ':
                n += 1
            else:
                tmp.append(s[m: n])
                while n < len(s) and s[n] == ' ':
                    n += 1
                m = n
        tmp.append(s[m:])
        p, q = 0, len(tmp) - 1
        while p < q:
            tmp[p], tmp[q] = tmp[q], tmp[p]
            p += 1
            q -= 1
        return ' '.join(tmp)
