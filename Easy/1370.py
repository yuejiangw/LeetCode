class Solution:
    def removeAll(self, s, a: str):
        while a in s:
            s.remove(a)
        return s

    def sortString(self, s: str) -> str:
        result = []
        while len(result) != len(s):
            tmp = list(s)
            while(tmp):
                minChar = min(tmp)
                result.append(minChar)
                self.removeAll(tmp, minChar)
            tmp = list(s)
            while(tmp):
                maxChar = max(tmp)
                result.append(maxChar)
                self.removeAll(tmp, maxChar)
        return ''.join(result)

if __name__ == "__main__":
    sol = Solution()
    test = 'rat'
    print(sol.sortString(test))