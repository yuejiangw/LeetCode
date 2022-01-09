from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        path = ''
        def backtracking(start, path):
            if start == len(s):
                res.append(path)
                return
            if s[start].isdigit():
                backtracking(start + 1, path + s[start])
            else:
                backtracking(start + 1, path + s[start].lower())
                backtracking(start + 1, path + s[start].upper())
        
        backtracking(0, path)
        return res

                    