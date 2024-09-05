from typing import List


class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        # dp 实现博弈问题，参考 https://leetcode.cn/problems/stone-game/description/
        n = len(nums)
        # dp[i][j][0] 代表 nums[i...j] 中先手可以取得的最高分
        # dp[i][j][1] 代表 nums[i...j] 中后手可以取得的最高分
        dp = [[[0, 0] for _ in range(n)] for _ in range(n)]

        # init
        for i in range(n):
            dp[i][i][0] = nums[i]
        
        # state transfer
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                # left 代表在 num[i...j] 中先手拿最左边的牌可以取得的最高分
                left = nums[i] + dp[i+1][j][1]
                # right 代表在 num[i...j] 中先手拿最右边的牌可以取得的最高分
                right = nums[j] + dp[i][j-1][1]
                if left > right:
                    dp[i][j][0] = left
                    # 如果对方先手拿走了 nums[i]，则我在下一次 num[i+1...j] 的选择中是先手
                    dp[i][j][1] = dp[i+1][j][0]
                else:
                    dp[i][j][0] = right
                    # 如果对方先手拿走了 nums[j]，则我在下一次 num[i...j-1] 的选择中是先手
                    dp[i][j][1] = dp[i][j-1][0]
        
        res = dp[0][n-1]
        return res[0] >= res[1]