class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 双指针，时间复杂度 O(n)，空间复杂度 O(1)
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True
