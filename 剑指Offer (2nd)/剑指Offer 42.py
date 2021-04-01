class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        DP，对于当前元素要么将其加入之前序列的和中，要么从当前元素开始重新求和
        状态转移方程为 max(dp[i-1] + nums[i], nums[i])
        '''
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
        return max(dp)