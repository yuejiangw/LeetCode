class Solution:
    """
    找到割点，分别对两边区域递归求解
    """

    def longestNiceSubstring(self, s: str) -> str:
        for i, c in enumerate(s):
            if c.lower() not in s or c.upper() not in s:
                return max(
                    self.longestNiceSubstring(s[:i]),
                    self.longestNiceSubstring(s[i + 1 :]),
                    key=len,
                )
        return s
