from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        # T: O(N)
        # S: O(N)
        n = len(shifts)
        total_shift = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            total_shift[i] = total_shift[i + 1] + shifts[i]

        res = ''
        for i, char in enumerate(s):
            shifted_char = chr(ord('a') + (ord(char) - ord('a') + total_shift[i]) % 26)
            res += shifted_char
        return res
