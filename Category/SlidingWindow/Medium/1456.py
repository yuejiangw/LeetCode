from collections import defaultdict

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = set(['a', 'e', 'i', 'o', 'u'])
        l, r = 0, 0
        res = 0
        curr_max_vowel_num = 0
        while r < len(s):
            c = s[r]
            r += 1
            if c in vowel:
                curr_max_vowel_num += 1
            while r - l > k:
                d = s[l]
                l += 1
                if d in vowel:
                    curr_max_vowel_num -= 1
            if r - l == k:
                res = max(res, curr_max_vowel_num)
        return res