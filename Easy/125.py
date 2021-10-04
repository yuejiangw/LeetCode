class Solution:
    def isPalindrome(self, s: str) -> bool:
        target = ""
        for letter in s:
            if (letter >= 'a' and letter <= 'z')\
                or (letter >= 'A' and letter <= 'Z')\
                or (letter >= '0' and letter <= '9'):
                target += letter.lower()
        i, j = 0, len(target) - 1
        while i <= j:
            if target[i] != target[j]:
                return False
            i += 1
            j -= 1
        return True