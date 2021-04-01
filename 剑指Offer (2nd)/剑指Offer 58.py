class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip().split(' ')[::-1]
        i = 0
        while i < len(s):
            if s[i] == '':
                del s[i]
            else:
                i += 1
        return ' '.join(s)