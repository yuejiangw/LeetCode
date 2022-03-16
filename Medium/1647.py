from typing import Counter


class Solution:
    def minDeletions(self, s: str) -> int:
        # Greedy
        # T: O(nlogn + n)
        # S: O(n)
        cnt = Counter(s)
        res = 0
        value = sorted(cnt.values())
        appear_nums = set()
        for i in range(len(value)):
            while value[i] > 0 and value[i] in appear_nums:
                value[i] -= 1
                res += 1
            if value[i] != 0:
                appear_nums.add(value[i])
        return res