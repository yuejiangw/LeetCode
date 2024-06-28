from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n, max_len, res = len(nums), 0, 0
        # dp[i] 代表以 nums[i] 结尾的最长上升子序列的长度
        dp = [1] * n
        # cnt[i] 代表以 nums[i] 结尾的最长上升子序列的个数
        cnt = [1] * n
        
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        cnt[i] = cnt[j]     # 重置计数
                    elif dp[j] + 1 == dp[i]:
                        cnt[i] += cnt[j]
            if dp[i] > max_len:
                max_len = dp[i]
                res = cnt[i]
            elif dp[i] == max_len:
                res += cnt[i]
        return res