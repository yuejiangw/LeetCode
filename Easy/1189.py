from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cnt1 = Counter(text)
        cnt2 = Counter('balloon')

        def is_larger():
            for k, v in cnt2.items():
                if cnt1.get(k, 0) < v:
                    return False
            return True

        res = 0
        while is_larger():
            cnt1 -= cnt2
            res += 1
        return res
