# 解法1：右移一位表示除以2
class Solution:
    def sumNums(self, n: int) -> int:
        return (pow(n, 2) + n) >> 1

# 解法2：递归，用 n 是否为0作为出口条件
class Solution:
    def sumNums(self, n: int) -> int:
        return n and n + self.sumNums(n - 1)
