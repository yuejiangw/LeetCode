class Solution:
    def removePalindromeSub(self, s: str) -> int:
        """ 
        s中只有a和b两种字符，因此要么1步要么2步
        如果s本身就是回文串，则1步，否则需要2步: 先删a再删b
        """
        return 1 if s == s[::-1] else 2
