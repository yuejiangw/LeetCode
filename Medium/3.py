class Solution:
    """ brute force, O(n^2) """
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        i, j = 0, 0
        while i < len(s):
            j = i + 1
            while j < len(s):
                if s[j] not in s[i:j]:
                    j += 1
                else:
                    break
            result = max(result, j - i)
            i += 1
        return result

from collections import defaultdict
class Solution:
    """ sliding window, O(n) """
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        window = defaultdict(int)
        i, j = 0, 0
        while j < len(s):
            c = s[j]
            j += 1
            window[c] += 1
            while window[c] > 1:
                d = s[i]
                i += 1
                window[d] -= 1
            res = max(res, j - i)
        return res