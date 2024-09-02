class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        curr_max_len = 1
        res = 1
        for i in range(1, len(s)):
            curr_max_len = curr_max_len + 1 if ord(s[i]) - ord(s[i - 1]) == 1 else 1
            res = max(res, curr_max_len)
        return res