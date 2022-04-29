from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:
        # T:  O(n * n!)
        # S: O(n)
        
        s = sorted(s)
        path = []
        res = []
        used = [False] * len(s)

        def backtracking():
            if len(path) == len(s):
                res.append(''.join(path))
                return
            for i in range(len(s)):
                if i > 0 and s[i] == s[i - 1] and not used[i - 1]:
                    continue
                if not used[i]:
                    used[i] = True
                    path.append(s[i])
                    backtracking()
                    path.pop()
                    used[i] = False
        
        backtracking()
        return res
