class Solution:
    def getSmallestString(self, s: str) -> str:
        # Greedy, 尽可能早地交换
        s = list(s)
        for i in range(len(s) - 1):
            a, b = int(s[i]), int(s[i + 1])
            if a % 2 == b % 2 and b < a:
                s[i], s[i + 1] = s[i + 1], s[i]
                break
        return ''.join(s)
