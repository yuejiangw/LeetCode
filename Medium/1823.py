class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        """解法1: 约瑟夫环递推公式，递归
        设初始队列长度为N，编号为1 - N, 报数每报到 M 则删除该数,
        最后剩下的数用 f(N, M) 表示，则 f(N, M) = (f(N-1, M) + M) % N
        """
        if n == 1:
            return n
        res = self.findTheWinner(n - 1, k) + k
        return n if res % n == 0 else res % n
    
    def findTheWinner(self, n: int, k: int) -> int:
        """解法2: 约瑟夫环递推公式，类似于动态规划
        设初始队列长度为N，编号为1 - N, 报数每报到 M 则删除该数,
        最后剩下的数用 f(N, M) 表示，则 f(N, M) = (f(N-1, M) + M) % N
        """
        res = 0
        # base case 下 n = 1，因此 i 从 2 开始累加
        for i in range(2, n + 1):
            res = (res + k) % i
        return res + 1

    def findTheWinner(self, n: int, k: int) -> int:
        """解法3: 队列模拟
        """
        s, Q = 0, [i for i in range(1, n + 1)]
        while len(Q) > 1:
            lost = (s + k - 1) % len(Q) # 确定该轮失败者的位置
            s = lost if (lost != len(Q) - 1) else 0 # 更新下一轮开始的人的下标
            del Q[lost] # 删除失败者
        return Q[0]