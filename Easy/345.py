class Solution:
    def isVowel(self, c):
        return c in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    def reverseVowels(self, s: str) -> str:
        s = list(s)
        i = 0   
        j = len(s) - 1
        while i < j:
            while not self.isVowel(s[i]) and i < j:
                i += 1
            while not self.isVowel(s[j]) and i < j:
                j -= 1
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return ''.join(s)