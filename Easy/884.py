from collections import Counter
from typing import List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # 拼接字符串 s1 + s2，返回拼接后字符串中只出现过一次的单词
        s = s1.strip().split() + s2.strip().split()
        counter = Counter(s)
        return [x for x in counter if counter[x] == 1]
