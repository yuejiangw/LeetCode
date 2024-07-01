class Solution:
    '''
    动态规划思想（一维）
    面对一个新的房子有两种选择：抢和不抢
    若是不抢，则当前房子的总钱数和上一所房子获得的钱数相同，即 dp[i-1]
    若是抢，因为不能抢劫相邻的房子，因此获得的钱数为 dp[i-2] + nums[i]
    求二者间较大的一个作为当前房子的选择，即为状态转移方程
    '''
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        return dp[-1]

class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i][0] 代表抢 nums[i] 的房子可以获得的最大利润
        # dp[i][1] 代表不抢 nums[i] 的房子可以获得的最大利润
        dp = [[0, 0] for _ in range(len(nums))]
        # init
        dp[0][0] = nums[0]
        # state transfer
        for i in range(1, len(nums)):
            # 对于当前 house 有两种选择：抢和不抢
            # 如果抢，则前一个房子就不能抢
            dp[i][0] = dp[i - 1][1] + nums[i]
            # 如果不抢则前一个房子可抢可不抢，找收益较大的一个数填入
            dp[i][1] = max(dp[i - 1])
        return max(dp[-1])