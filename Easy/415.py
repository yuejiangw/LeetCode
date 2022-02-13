class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j, carry = len(num1) - 1, len(num2) - 1, 0
        res = ''
        while i >= 0 or j >= 0:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            tmp = n1 + n2 + carry
            carry = tmp // 10
            res = str(tmp % 10) + res
            i -= 1
            j -= 1
        return str(carry) + res if carry else res


class Solution:
    """ 思路与链表相加类似 """
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = num1[::-1]
        num2 = num2[::-1]
        carry = 0
        i, j = 0, 0
        res = ''
        while i < len(num1) or j < len(num2) or carry:
            n = carry
            if i < len(num1):
                n += int(num1[i])
                i += 1
            if j < len(num2):
                n += int(num2[j])
                j += 1
            res += str(n % 10)
            carry = n // 10
        return res[::-1]
