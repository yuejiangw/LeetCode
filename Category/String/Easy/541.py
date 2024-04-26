class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        def rev(s, i, j):
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        s = list(s)
        for i in range(0, len(s), 2 * k):
            if i + k <= len(s):
                rev(s, i, i + k - 1)
                continue
            rev(s, i, len(s) - 1)
        return ''.join(s)
