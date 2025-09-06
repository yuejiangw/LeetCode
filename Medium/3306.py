from collections import defaultdict

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowel = {'a', 'e', 'i', 'o', 'u'}
        res = r = 0
        window1 = defaultdict(int)
        count1 = l1 = 0
        window2 = defaultdict(int)
        count2 = l2 = 0
        while r < len(word):
            c = word[r]
            r += 1
            if c in vowel:
                window1[c] += 1
                window2[c] += 1
            else:
                count1 += 1
                count2 += 1
            while len(window1) == 5 and count1 >= k:
                d1 = word[l1]
                l1 += 1
                if d1 in vowel:
                    window1[d1] -= 1
                    if window1[d1] == 0:
                        del window1[d1]
                else:
                    count1 -= 1
            while len(window2) == 5 and count2 > k:
                d2 = word[l2]
                l2 += 1
                if d2 in vowel:
                    window2[d2] -= 1
                    if window2[d2] == 0:
                        del window2[d2]
                else:
                    count2 -= 1
            res += l1 - l2
        return res
