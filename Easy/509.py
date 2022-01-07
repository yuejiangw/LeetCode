class Solution:
    """ 普通递归 """
    def fib(self, n: int) -> int:
        fibs = [0, 1]
        for i in range(2, n + 1):
            fibs.append(fibs[i - 1] + fibs[i - 2])
        return fibs[n]


class Solution:
    """ 迭代，空间复杂度 O(1) """
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        pre_1, pre_2 = 0, 1
        for i in range(2, n):
            tmp = pre_1
            pre_1 = pre_2
            pre_2 += tmp
        return pre_1 + pre_2