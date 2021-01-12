class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sSplit = s.split(' ')
        for i in range(len(sSplit) - 1, -1, -1):
            if sSplit[i] != "":
                return len(sSplit[i])
        return 0