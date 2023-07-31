from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[i] 表示字符串长度为i时能否被成功拆分
        dp = [False] * (len(s) + 1)
        dp[0] = True

        # 递推公式：如果dp[j]为True，并且s[j:i]还在wordDict中可以匹配，则dp[i]也为True
        for i in range(1, len(s) + 1):
            for j in range(i):
                word = s[j: i]
                if dp[j] == True and word in wordDict:
                    dp[i] = True
        return dp[-1]
