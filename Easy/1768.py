class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # T: O(n), S: O(1)
        res = ""
        i, j = 0, 0
        while i < len(word1) or j < len(word2):
            if i < len(word1):
                res += word1[i]
            if j < len(word2):
                res += word2[j]
            i += 1
            j += 1
        return res