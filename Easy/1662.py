class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        str1, str2 = "", ""
        for w1 in word1:
            str1 += w1
        for w2 in word2:
            str2 += w2
        return str1 == str2