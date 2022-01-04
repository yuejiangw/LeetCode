from typing import List


class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        pairs = [['1', '1'], ['6', '9'], ['8', '8'], ['9', '6']]

        def dfs(x):
            if x == 0:
                return [""]
            if x == 1:
                return ['0', '1', '8']
            res = []
            # 中心对称，左右同时添加，因此每次递归 x 的长度要减2
            for num in dfs(x - 2):
                for l, r in pairs:
                    res.append(l + num + r)
                # 0不能用作开头，所以 x != n 的情况下才能添加0
                if x != n:
                    res.append('0' + num + '0')
            return res

        return dfs(n)

    def strobogrammaticInRange(self, low: str, high: str) -> int:
        low_len = len(low)
        high_len = len(high)

        min_len = min(low_len, high_len)
        max_len = max(low_len, high_len)

        res = 0
        for n in range(min_len, max_len + 1):
            for s in self.findStrobogrammatic(n):
                if int(low) <= int(s) <= int(high):
                    res += 1
        return res
