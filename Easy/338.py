from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        # 如果 n 是偶数，则 f(n) = f(n // 2)，
        # 因为除法相当于右移一位，高位补0，对于 1 的数量来说不变；
        # 如果 n 是奇数，则 f(n) = f(n-1) + 1，因为 n 是偶数
        # 并且 n 的最后一位一定为 0
        res = [0]
        for i in range(1, n + 1):
            if i % 2 == 0:
                res.append(res[i // 2])
            else:
                res.append(res[i - 1] + 1)
        return res
