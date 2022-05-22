from typing import List
from collections import defaultdict


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # 假设让每个单词都做最长字符链串的最后一个，逆向思维
        # 可以通过删除一个字符后得到的更短新单词来作为其前一个单词
        # 通过这些更短新单词的最优解，来得到当前单词的最优解
        # T: O(nlogn + mn), n = len(words), m = max(word)
        # S: O(n)
        dp = defaultdict(int)

        # 先排序，后对每个单词进行删一个字母的转移
        for s in sorted(words, key=len):
            # s[:i] + s[i + 1:] 为删除 s[i] 后得到的更短新单词
            # dp[s[:i] + s[i + 1:]] + 1 for i in range(len(s))
            # 为列表推导式，通过它得到了所有更短新单词的最优解
            dp[s] = max(dp[s[:i] + s[i+1:]] + 1 for i in range(len(s)))
        return max(dp.values())