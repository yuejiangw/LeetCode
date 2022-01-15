class Solution:
    def totalMoney(self, n: int) -> int:
        res = [0] * (n + 1)
        res[1] = 1
        for i in range(2, n + 1):
            if i % 7 == 1:
                res[i] = res[i - 7] + 1
            else:
                res[i] = res[i - 1] + 1
        return sum(res)
