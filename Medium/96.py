class Solution:
    def numTrees(self, n: int) -> int:
        if n <= 2:
            return n

        # 令 dp[i] 表示 i 个结点可以生成的二叉树的数量
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        
        # 对于 i 个结点来说，选取一个结点作为根结点，则剩下的 i - 1 个结点可以
        # 作为左、右子树的结点。设j代表左子树结点的数量，因此右子树结点的数量就是i - 1- j。
        # 则不难看出dp[i] = dp[j] * dp[i-1-j] (0<=j<=i-1)
        for i in range(3, n + 1):
            for j in range(0, i):
                dp[i] += dp[j] * dp[i - 1 - j]
        return dp[n]