class Solution:
    def maxDepth(self, s: str) -> int:
        results = []
        tmp = 0
        for i in s:
            if i == "(":
                tmp += 1
            elif i == ")":
                results.append(tmp)
                tmp -= 1
        return 0 if results == [] else max(results)