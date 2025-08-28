from collections import defaultdict

class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        '''
        T: O(N)
        S: O(1) as s only contains lowercased English letters
        '''
        l = r = 0
        window = defaultdict(int)
        res = 0
        while r < len(s):
            c = s[r]
            r += 1
            window[c] += 1
            if r - l < k:
                continue
            if len(window) == r - l:
                res += 1
            d = s[l]
            l += 1
            window[d] -= 1
            if window[d] == 0:
                del window[d]
        return res