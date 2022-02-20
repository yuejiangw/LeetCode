from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        N = len(bits)
        i = 0
        while i < N - 1:
            if bits[i] == 1:
                i += 2
            else:
                i += 1
        return True if i == N - 1 else False