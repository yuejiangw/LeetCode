from typing import List


class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        """
        题目翻译：
        对于 query，是否可以在 pattern 的基础上，在 pattern 的任意
        位置上加上任意数目（包括0个）的小写字母直到得到 query
        """

        def is_match(query, pattern) -> bool:
            j = 0
            for c in query:
                if j < len(pattern) and c == pattern[j]:
                    j += 1
                elif c.isupper():
                    return False
            return j == len(pattern)

        return [is_match(query, pattern) for query in queries]
