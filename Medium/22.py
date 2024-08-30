from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []

        def backtracking(n, left, right):
            if left + right == 2 * n:
                res.append(''.join(path))
                return
            if left < n:
                path.append('(')
                backtracking(n, left + 1, right)
                path.pop()
            if right < left:
                path.append(')')
                backtracking(n, left, right + 1)
                path.pop()
        backtracking(n, 0, 0)
        return res
