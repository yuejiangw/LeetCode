from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        sub_string = []
        res = []

        def backtracking(s, start_index):
            if start_index >= len(s):
                res.append(sub_string[:])
                return
            for i in range(start_index, len(s)):
                p = s[start_index: i + 1]
                if p == p[::-1]:
                    sub_string.append(p)
                else:
                    continue

                backtracking(s, i + 1)
                sub_string.pop()
        backtracking(s, 0)
        return res