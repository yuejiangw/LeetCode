from typing import List


class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        # Greedy
        # T: O(N)
        # S: O(1)
        if finalSum % 2 == 1:
            return []
        
        res = []
        remain = finalSum
        current = 0
        for i in range(2, finalSum, 2):
            remain -= i
            if remain <= i:
                remain += i
                break
            res.append(i)
        res.append(remain)
        return res
            