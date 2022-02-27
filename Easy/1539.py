from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i, j = 0, 1
        while i < len(arr) and k > 0:
            if j == arr[i]:
                j += 1
                i += 1
            else:
                j += 1
                k -= 1
        return j - 1 if k == 0 else j + k - 1