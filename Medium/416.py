from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # 无法分割成两个子集
        if len(nums) < 2:
            return False
        
        # 数组元素和为奇数
        if sum(nums) % 2 != 0:
            return False
        
        # 背包问题
        target = sum(nums) // 2
        dp = [0 for _ in range(target + 1)]
        for i in range(len(nums)):
            j = target
            while j >= nums[i]:
                dp[j] = max(dp[j], dp[j - nums[i]] + nums[i]) 
                j -= 1
        return dp[target] == target