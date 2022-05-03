from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # T: O(N)
        # S: O(1), 因为字符集只包含英文，数字，空格，长度固定
        window = defaultdict(int)
        i, j = 0, 0
        res = 0
        while j < len(s):
            c = s[j]
            j += 1
            window[c] += 1
            while i < j and window[c] > 1:
                d = s[i]
                i += 1
                window[d] -= 1
            res = max(res, j - i)
        return res