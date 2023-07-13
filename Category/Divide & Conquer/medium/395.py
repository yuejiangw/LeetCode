from collections import defaultdict


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        """
        分治法，假设 len(s) = N
        T: O(26 * N)，因为每次递归调用都会完全去除某个字符，因此递归深度最多为 26
        S: O(26 ^ 2)，因为递归深度为 O(26)，每层递归需要开辟 O(26) 的额外空间
        """
        if not s:
            return 0
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)
