class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        dp = [0 for _ in range(15001)]
        all_sum = sum(stones)
        target = all_sum // 2
        for i in range(len(stones)):
            j = target
            while j >= stones[i]:
                dp[j] = max(dp[j], dp[j - stones[i]] + stones[i])
                j -= 1
        return all_sum - dp[target] - dp[target]