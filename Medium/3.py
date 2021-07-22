class Solution:
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