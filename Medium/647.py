class Solution:
    def isPalindromic(self, s) -> bool:
        '''判断s是否是回文串'''
        return s == s[::-1]
    
    def getSubstrings(self, s: str) -> List[str]:
        '''获取所有子串'''
        result = []
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                result.append(s[i:j])
        return result

    def countSubstrings(self, s: str) -> int:
        substrings = self.getSubstrings(s)
        result = list(map(self.isPalindromic, substrings))
        return result.count(True)
