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