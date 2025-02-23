class Solution:
    def isPalindrome(self, x: int) -> bool:
        # T: O(log10(n)), S: O(1)
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        
        revertedNumber = 0
        while x > revertedNumber:
            revertedNumber = revertedNumber * 10 + x % 10
            x //= 10

        return x == revertedNumber or x == revertedNumber // 10


class Solution:
    def isPalindrome(self, x: int) -> bool:
            # T: O(n), S: O(1)
            return True if str(x) == str(x)[::-1] else False