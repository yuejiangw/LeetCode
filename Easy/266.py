from collections import Counter


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        # Time: O(N)
        # Space: O(N)
        even, odd = 0, 0
        for v in Counter(s).values():
            if v % 2 == 0:
                even += 1
            else:
                odd += 1
        return odd <= 1